// RADIO BUTTONS
// relevance of the video
const radioButton_relevant = document.getElementById("id-relevant");
const radioButton_no_relevant = document.getElementById("id-no-relevant");
// video content
const radioButton_nnc = document.getElementById("id-no-negative");
const radioButton_nc = document.getElementById("id-negative");
const radioButton_hsc = document.getElementById("id-hate-speech");
// confidence in answers
const radioButton_nms = document.getElementById("id-no-muy-seguro");
const radioButton_s = document.getElementById("id-seguro");
const radioButton_ms = document.getElementById("id-muy-seguro");
// hs factors
const radioButton_f1 = document.getElementById("id-factor1");
const radioButton_f2 = document.getElementById("id-factor2");
const radioButton_f3 = document.getElementById("id-factor3");

// BUTTONS
const button_nextvideo = document.getElementById("id-btn-video-annotation");

// DIVS
const div_relevant = document.getElementById("class-relevant-or-not");
// video content
const div_hs_or_not = document.getElementById("class-hs-or-not");
// confidence in answers
const div_confidence = document.getElementById("class-confidence");
// case: hate-speech content
const div_hs_selected = document.getElementById("class-hs-selected");
const div_hs_factor = document.getElementById("class-hs-factor");

// others
//const div_hs_guideline = document.getElementById("div-hs-content");

// ABOUT: RELEVANT-OR-NOT
// relevant
radioButton_relevant.addEventListener("change", () => {
    if (radioButton_relevant.checked){
        div_hs_or_not.style.display="block";
        // Reset button
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else {
        button_nextvideo.style.display = "none";
    }
});
// NO relevant
radioButton_no_relevant.addEventListener("change", () => {
    if (radioButton_no_relevant.checked){
        // Mostrar botón
        button_nextvideo.style.display = "block";
        // show comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "block";
        document.querySelector('textarea[name="txt-notes"]').value = '';
        // Ocultar CONFIDENCE
        const div_confidence = document.getElementById('class-confidence');
        div_confidence.style.display="none";
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        // Ocultar CONTENIDO
        const div_hs_or_not = document.getElementById('class-hs-or-not');
        div_hs_or_not.style.display="none";
        const contentRadios = document.getElementsByName('hs-tag');
        contentRadios.forEach(radio => {
            radio.checked = false;  // Desmarcar todos los radio buttons
        });
        document.getElementById('id-content-default').checked = true;  // Marcar el valor predeterminado (-1)
        // Ocultar caso: HATE-SPEECH
        const div_hs_selected = document.getElementById('class-hs-selected');
        div_hs_selected.style.display="none";
        // Ocultar FACTOR
        const div_hs_factor = document.getElementById('class-hs-factor');
        div_hs_factor.style.display="none";
        const factorRadios = document.getElementsByName('factor-tag');
        factorRadios.forEach(radio =>{
            radio.checked = false;
        })
        document.getElementById('id-factor-neutral').checked = true;
    } else {
        button_nextvideo.style.display = "none";
    }
});

// ABOUT: VIDEO CONTENT (check radio buttons)
// case: no negative content / neutral
radioButton_nnc.addEventListener("change", () => {
    if (radioButton_nnc.checked){
        // Ocultar caso: HATE-SPEECH
        const div_hs_selected = document.getElementById('class-hs-selected');
        div_hs_selected.style.display="none";
        // Ocultar FACTOR
        const div_hs_factor = document.getElementById('class-hs-factor');
        div_hs_factor.style.display="none";
        const factorRadios = document.getElementsByName('factor-tag');
        factorRadios.forEach(radio =>{
            radio.checked = false;
        })
        document.getElementById('id-factor-neutral').checked = true;
        // Reset CONFIDENCE
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        div_confidence.style.display = "block";
        // Reset BUTTON
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else {
        div_confidence.style.display = "none";
        button_nextvideo.style.display = "none";
    }
});
// case: negative content
radioButton_nc.addEventListener("change", () => {
    if (radioButton_nc.checked){
        // Ocultar caso: HATE-SPEECH
        const div_hs_selected = document.getElementById('class-hs-selected');
        div_hs_selected.style.display="none";
        // Ocultar FACTOR
        const div_hs_factor = document.getElementById('class-hs-factor');
        div_hs_factor.style.display="none";
        const factorRadios = document.getElementsByName('factor-tag');
        factorRadios.forEach(radio =>{
            radio.checked = false;
        })
        document.getElementById('id-factor-neutral').checked = true;
        // Reset CONFIDENCE
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        div_confidence.style.display = "block";
        // Reset BUTTON
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else {
        button_nextvideo.style.display = "none";
    }
});
// case: hate-speech content
radioButton_hsc.addEventListener("change", () => {
    if (radioButton_hsc.checked){
        // Reset CONFIDENCE
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        div_confidence.style.display="none";
        //
        div_hs_selected.style.display="block";
        // show FACTOR
        div_hs_factor.style.display="block";
        // Reset BUTTON
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else {
        button_nextvideo.style.display = "none";
    }
});

// ABOUT: FACTOR (check radio buttons)
// factor 1
radioButton_f1.addEventListener("change", () => {
    if(radioButton_f1.checked){
        // Reset CONFIDENCE
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        div_confidence.style.display = "block";
        //button_nextvideo.style.display = "block";
        // Reset BUTTON
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else{
        button_nextvideo.style.display = "none";
    }
})
// factor 2
radioButton_f2.addEventListener("change", () => {
    if(radioButton_f2.checked){
        // Reset CONFIDENCE
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        div_confidence.style.display = "block";
        //button_nextvideo.style.display = "block";
        // Reset BUTTON
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else{
        button_nextvideo.style.display = "none";
    }
})
// factor 3
radioButton_f3.addEventListener("change", () => {
    if(radioButton_f3.checked){
        // Reset CONFIDENCE
        const confidenceRadios = document.getElementsByName('confidence-tag');
        confidenceRadios.forEach(radio=> {
            radio.checked = false;
        })
        document.getElementById('id-confidence-nan').checked = true;
        div_confidence.style.display = "block";// Reset BUTTON
        button_nextvideo.style.display = "none";
        // Reset comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "none";
        document.querySelector('textarea[name="txt-notes"]').value = '';
    } else{
        button_nextvideo.style.display = "none";
    }
})


// ABOUT: CONFIDENCE (check radio buttons)
// no muy seguro
radioButton_nms.addEventListener("change", () =>{
    if(radioButton_nms.checked){
        // show comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "block";
        // show button save and continue
        button_nextvideo.style.display = "block";
    }else{
        button_nextvideo.style.display = "none";
    }
})
// seguro
radioButton_s.addEventListener("change", () =>{
    if(radioButton_s.checked){
        // show comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "block";
        // show button save and continue
        button_nextvideo.style.display = "block";
    }else{
        button_nextvideo.style.display = "none";
    }
})
// muy seguro
radioButton_ms.addEventListener("change", () =>{
    if(radioButton_ms.checked){
        // show comments
        const div_comments = document.getElementById("class-comments");
        div_comments.style.display = "block";
        // show button save and continue
        button_nextvideo.style.display = "block";
    }else{
        button_nextvideo.style.display = "none";
    }
})


// CLICK ON: info for guidelines
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

// ABOUT: SENDING VIDEO ANNOTATIONS
// CLICK ON: button to submit the form responses
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

// ABOUT: REQUESTING ANOTHER BATCH OF VIDEOS
// CLICK ON: button for next batch assignment
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
