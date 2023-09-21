# Video Annotation Web App 
This is a web app to annotate the video dataset built up for the hate speech detection task. 

- [Video Annotation Web App](#video-annotation-web-app)
  - [Summary](#summary)
  - [Getting Started](#getting-started)
      - [Code Structure](#code-structure)
  - [Media Coverage](#media-coverage)

# Summary
A video dataset was built as part of the project _Hate speech detection in videos using multimodal information_. The goal is to provide a video dataset focused on Mexican Spanish-based language for the hate speech detection task. 

For the video dataset, it is planned that each video will be assigned a tag whether it contains hate speech-related content or not. To ensure a variety of opinions when assigning the final tag to each video, each video will be shown to at least 3 different annotators. Then, a majority vote will decide the final tag for each video.

An annotator's guideline is provided. The guideline `guía de anotación para dataset de videos de discurso de odio` is available in Spanish to facilitate it to our annotators. 

# Getting Started
## Code Structure
```
├── batch_files                # csv files that contains information of the videos of each batch
├── etiquetados                # csv files where each one contains the labels of each user
├── instance                   # sqlite database file 
│   ├── df.sqlite
├── static                     # css and javascript files
│   ├── pool-videos            # videos (.mp4) that are going to be annotated
├── templates                  # html files
├── venv
├── app.py                     # main script to run the app
├── batches_annotators.py
├── batches_dict.txt
├── def_funcionts.py
├── guía de anotación para dataset de videos de discurso de odio     # annotator's guideline
└── README.md
```
## Sharing the webapp
We used [ngrok](https://ngrok.com/) to share our app. So, if you plan to use it too a download and configuration for ngrok is required. 

To share the web app first execute the file `app.py` on your console:
```bash
python app.py
```
by default, it would be running on the port 5000. 
Then, open another bash on the location where you installed the `ngrok.exe` file and execute:
```bash
ngrok http port=5000
```
If there is no problem you will be able to get a URL that allows you to share the app.

# Media Coverage
