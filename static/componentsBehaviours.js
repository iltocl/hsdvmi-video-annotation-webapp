const hs_radioButton = document.getElementById("id-hate-speech");
const nhs_radioButton = document.getElementById("id-no-hate-speech");

const radioButton_relevant = document.getElementById("id-relevant");
const radioButton_no_relevant = document.getElementById("id-no-relevant");

const div_hs_selected = document.getElementById("class-hs-selected");
const div_nhs_selected = document.getElementById("class-nhs-selected")

const button_nextvideo = document.getElementById("id-btn-video-annotation");

const div_hs_guideline = document.getElementById("div-hs-content");

// change of radio buttons for hate-speech and non-hate-speech content 
hs_radioButton.addEventListener("change", () => {
    if (hs_radioButton.checked){

        div_nhs_selected.style.display = "none";
        div_hs_selected.style.display = "block";
        button_nextvideo.style.display = "block";
        div_hs_guideline.style.display = "block";

    } else {
        button_nextvideo.style.display = "none";
    }
});

nhs_radioButton.addEventListener("change", () => {
    if (nhs_radioButton.checked){
        div_hs_selected.style.display = "none";
        div_nhs_selected.style.display = "block";
        button_nextvideo.style.display = "block";
    } else {
        button_nextvideo.style.display = "none";
    }
});

// click on info for guidelines
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

// click on button to submit the form responses
function submitForm() {
    // disable button after one click
    document.getElementById('id-btn-video-annotation').disabled = true;
    
    // form data to be processed
    var formData = new FormData(document.getElementById('myForm'));
    // send the POST to the route /submit_to_db
    fetch('/submit_to_db', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/next';
        } else {
            alert('Error al pasar a siguiente página');
            //document.getElementById("id-btn-next-batch").style.display = "none";
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
    // prevent sending "default" form
    return false;
}







//
//

// click on button for next batch assignment
//function handleClick() {
  // disable the button after one click
  //document.getElementById("id-btn-next-batch").disabled = true;
//}
function clickOnNextBatch() {
    // disable button after one click
    document.getElementById('id-btn-next-batch').disabled = true;
    
    // request to server, assign new batch to the user
    fetch('/asignar_nuevo_batch', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/login';
        } else {
            alert('Por el momento no hay más videos para etiquetar');
            document.getElementById("id-btn-next-batch").style.display = "none";
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}




