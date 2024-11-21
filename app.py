# !pip install flask-ngrok

"""
HSDVMI Video Annotation webapp
|-> static: here goes the folder with all the videos to be annotated

last edited: 2023-09-11
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import os, json, csv
#import batches_annotators, def_functions
import my_functions

# -----------------------
# FLASK APP
# -----------------------
app = Flask(__name__)

# -----------------------
# SQL ALCHEMY FOR THE DATABASE
# -----------------------
# connect flask-sqlalchemy with a database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "secret-key-hsdvmi"
# initialize flask-sqlalchemy extension
db = SQLAlchemy()
# initialize LoginManager to be able to log in and out 
#login_manager = LoginManager(app)
login_manager = LoginManager()
login_manager.init_app(app)

# create 'User' model for the database
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # changed initialization to 0
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    current_video_index = db.Column(db.Integer)
    batch_id = db.Column(db.String(250), nullable=False)
# initialize app with extension
db.init_app(app)
# create database within app context
with app.app_context():
    db.create_all()
# create a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(int(user_id))

# -----------------------
# GLOBAL VARIABLES
# -----------------------
# path where the annonations by users will be saved
global DIR_PATH_ETIQUETADOS
DIR_PATH_ETIQUETADOS = "etiquetados/" 
# dictionary to manage the batch per user assignations
global lst_batches
lst_batches = os.listdir("batch_files/") # directory with all the .csv files, one per batch
file_path = "batches_dict.txt" # dictionary with the assignations, batch_m: [annotator_a, annotator_b]
if os.path.exists(file_path):
    print(f'The file "{file_path}" exists.')
    with open(file_path, 'r') as file:
        json_string = file.read()
        batch_dict = json.loads(json_string)
        print('\nDictionary loaded successfully:')
        print(batch_dict)        


# -----------------------
# APP ROUTES
# -----------------------
# route for the home page
@app.route("/")
def home():
    print("-----------------------\n/\n-----------------------")
    print("-----------------------\nhome.html\n-----------------------")
    return render_template('home.html')

# route for the registration page 
@app.route("/register", methods=["GET", "POST"])
def register():
    print("-----------------------\n/register\n-----------------------")
    print("-----------------------\nsign_up.html\n-----------------------")
    if request.method == "POST":
        # if user made a POST request create a new user
        username = request.form.get("username")
        password = request.form.get("password")
        # check if that user already exists on the database
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user:
            message = "Ese nombre de usario ya está en uso. Favor de usar otro."
            return render_template('sign_up.html', message=message)
        else:
            user = Users(username=username,
                        password=password,
                        current_video_index=0,
                        batch_id="")
            # add the user to the database
            db.session.add(user)
            db.session.commit()
            print("\n-----------------------ADDED USER TO THE DB")
            print("DB ID", user.id)
            print("DB USER", user.username)
            print("DB PASSWORD",user.password) 
            print("DB CURRENT_VIDEO_INDEX",user.current_video_index)
            print("DB BATCH_ID", user.batch_id) 
            # assign a batch to the annotator
            try:
                # there are still available batches
                # assign a batch to the annotator 
                global updated_batch_dict, exception_occurred
                batch, updated_batch_dict, exception_occurred = my_functions.assign_bunch_to_annotator(user.id, batch_dict)
                # update the database
                user.batch_id = batch
                db.session.commit()
                # update the dictionary
                file_path = "batches_dict.txt"
                json_string = json.dumps(updated_batch_dict)
                with open(file_path, 'w') as file:
                    file.write(json_string)
                print(f'The file "{file_path}" was updated.')
                print("-----------------------\nUpdated DB BATCH_ID", user.batch_id, batch)
                return redirect(url_for("login"))
            except:
                # there are no more available batches
                return render_template("no.html")

    # if user mades a GET request render the template
    return render_template("sign_up.html")

# route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    print("-----------------------\n/login\n-----------------------")
    print("-----------------------\nlogin.html\n-----------------------")
    # if user mades a POST request 
    if request.method == "POST":
        # verify the 'username' and the 'password'
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user:
            # check if the password entered is the same as the user's password
            if user.password == request.form.get("password"):
                print("-----------------------\nLOGIN USER", user.get_id())
                login_user(user)
                print("DB CURRENT_VIDEO_INDEX", user.current_video_index)
                print("DB batch_id", user.batch_id)
                # load batch file that corresponds to the user
                csv_batch_file = "batch_files/" + user.batch_id
                lst_videos_ids, total_videos = my_functions.csv_batch_to_list(csv_batch_file)
                # check if there are available videos to annotate
                if user.current_video_index == total_videos or user.current_video_index > total_videos:
                    print("-----------------------\nLISTA TERMINADA")
                    # there are no more available videos to annotate from the batch
                    message = "Terminaste la lista de videos que te fue asignada."
                    return render_template('end.html', message=message)
                else:
                    # there are videos from the batch that need to be annotated
                    print("-----------------------\nMOSTRAR VIDEOS")
                    login_user(user)
                    print("User logged in successfully. DB USER ID", user.id)
                    #return redirect(url_for("serve_video", user=user.id))
                    return redirect(url_for("serve_video"))
            else:
                message = "La contraseña es incorrecta. Por favor vuelve a intentar."
                return render_template('login.html', message=message)
        else:
            message = "El nombre de usuario es incorrecto. Por favor vuelve a intentar."
            #return redirect(url_for("login"))
            return render_template('login.html', message=message)  
    # if user mades a GET request render the template
    return render_template("login.html")

# route to show the "current" video that the user has to annotate 
#@app.route("/video/<string:user>", methods=["GET", "POST"])
#def serve_video(user):
@app.route("/video", methods=["GET", "POST"])
def serve_video():
    print("-----------------------\n/video\n-----------------------")
    print("-----------------------\nvideo.html\n-----------------------")
    #print(f"User received from login: {user}")
    # session of the user that logged-in
    if current_user.is_authenticated:
        # load batch file that corresponds to the user
        csv_batch_file = "batch_files/" + current_user.batch_id
        lst_videos_ids, total_videos = my_functions.csv_batch_to_list(csv_batch_file)
        if current_user.current_video_index < total_videos:
            video_id = lst_videos_ids[current_user.current_video_index]
            #video_path = f'static/videos/{video_id}'
            #video_path = f'static/230607-filtered-videos-n05-from-hs-word-seeds-sre/{video_id}'
            video_path = f'static/pool-videos/{video_id}'
            print("VIDEO_PATH", video_path)
            message = "Annotación de Video %s / %s por usuario: %s" % (current_user.current_video_index, total_videos, current_user.username)
            
            return render_template('video.html', video_path=video_path, message=message)

    else:
        return redirect(url_for("login")) 
    
@app.route("/submit_to_db", methods=["GET","POST"])
def submit_to_db():
    print("-----------------------\n/submit_to_db\n-----------------------")
    # session of the user that logged-in
    if current_user.is_authenticated:
        # load batch file that corresponds to the user
        csv_batch_file = "batch_files/" + current_user.batch_id
        lst_videos_ids, total_videos = my_functions.csv_batch_to_list(csv_batch_file)
        """
        Obtained data from the form
        """
        # Q0. Is the video relevant?
        relevant_tag = request.form['relevant-tag']
        print("TAG RELEVANT", relevant_tag)
        # Q1. What content is it [0,1,2]=[neutral, innapropriate, hate-speech]
        hs_tag = request.form['hs-tag']
        print("TAG HATE SPEECH", hs_tag)
        # factor, discrim, sexism, others [1,2,3]
        #factor_tags = request.form.getlist('factor-tag')
        #print("TAG FACTOR", factor_tags)
        factor_tag = request.form['factor-tag']
        print("TAG FACTOR", factor_tag)
        # confidence tag
        confidence_tag = request.form['confidence-tag']
        print("TAG CONFIDENCE")
        # individual/group
        #target_tag = request.form['target-tag']
        #print("TAG TARGET", target_tag)
        # communication, txt, audio...
        #communication_tags = request.form.getlist('communication-tag')
        #print("TAG COMMUNICATION", communication_tags)
        # intention, physical attack, disapproval, mocking
        #intention_tags = request.form.getlist('intention-tag')
        #print("TAG INTENTION", intention_tags)
        # additional comments
        notes = request.form['txt-notes']
        print("NOTES", notes)
        #if hs_tag == 1:
        #    relevant_tag = 1
        # saving the annotations into a csv file
        file_path = DIR_PATH_ETIQUETADOS + current_user.batch_id[:-4] + "_" + current_user.username + "_labels.csv"
        video_id = lst_videos_ids[current_user.current_video_index]
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([current_user.username,
                            video_id,
                            relevant_tag,
                            hs_tag,
                            factor_tag,
                            confidence_tag,
                            notes])
        # update the current_video_index on the database
        try:
            current_user.current_video_index += 1
            db.session.commit()
            db.session.flush()
            print("DB CURRENT_VIDEO_INDEX UPDATED", current_user.current_video_index)
            print("-----------------------\nDB was updated")
            return jsonify(success=True)
        except:
            print("\nError in updating current_video_index\n")
        #return next_video()
    else:
        return jsonify(success=False), redirect(url_for("login"))
    
# route to continue to the next video 
@app.route('/next', methods=['GET','POST'])
def next_video():
    print("-----------------------\n/next\n-----------------------")
    # session of the user that logged-in
    if current_user.is_authenticated:
        # load batch file that corresponds to the user
        csv_batch_file = "batch_files/" + current_user.batch_id
        lst_videos_ids, total_videos = my_functions.csv_batch_to_list(csv_batch_file)
        if current_user.current_video_index < total_videos:
            video_id = lst_videos_ids[current_user.current_video_index]
            #video_path = f'static/videos/{video_id}'
            #video_path = f'static/230607-filtered-videos-n05-from-hs-word-seeds-sre/{video_id}'
            video_path = f'static/pool-videos/{video_id}'
            print("VIDEO_PATH", video_path)
            message = "Annotación de Video %s / %s por usuario: %s" % (current_user.current_video_index, total_videos, current_user.username)
            
            return render_template('video.html', video_path=video_path, message=message)
        else:
            message = "Terminaste la lista de videos que te fue asignada."
            return render_template('end.html', message=message)
    else:
        return redirect(url_for("login")) 

# route to assign a new batch to the user
@app.route('/asignar_nuevo_batch', methods=['GET', 'POST'])
def asignar_nuevo_batch():
    print("-----------------------\n/asignar_nuevo_batch\n-----------------------")
    # session of the user that logged-in
    if current_user.is_authenticated:
        try:
            # assign a new batch to the user
            global exception_occurred
            new_batch, updated_batch_dict, exception_occurred = my_functions.assign_bunch_to_annotator(current_user.id, batch_dict)
            current_user.batch_id = new_batch
            # reset the current_video_index to 0
            current_user.current_video_index = 0
            db.session.commit()
            db.session.flush()
            
            # ------------------------------------------------------------------------------------------
            print("----------------------------------------------------------- assing new batch")
            print("DB BATCH_ID UPDATED", current_user.batch_id, new_batch, current_user.current_video_index)
             # Cerrar la sesión del usuario
            logout_user()
            print("Logout to redirect to login")
            # ------------------------------------------------------------------------------------------
            # updating the json string dictionary
            file_path = "batches_dict.txt"
            json_string = json.dumps(updated_batch_dict)
            with open(file_path, 'w') as file:
                file.write(json_string)
            print(f'The file "{file_path}" was updated.')

            # Redirige a la página de inicio de sesión o a donde prefieras
            return jsonify(success=True) #, redirect(url_for("login"))
            
            #return jsonify(success=True)
        except:
            return jsonify(success=False)
    else:
        return redirect(url_for("login"))   

# route to logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

# -----------------------
# APP MAIN
# -----------------------
if __name__ == "__main__":
    # by default on port=5000
    app.run()