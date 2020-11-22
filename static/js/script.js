$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    $('#invitees').val('');
    M.textareaAutoResize($('#invitees'));
});

// Functions below are used to validate Difficulty qty matches Questions qty
// Couple with "if difficulty_total == quiz_details['questions']:" in def(create) in app.py
if(document.getElementById("questions")) {
    document.getElementById("questions").addEventListener("keyup", getQuestionsDataFn);
}

function getQuestionsDataFn() {
    questionsPerRound = parseInt(document.getElementById('questions').value);

    document.getElementById('easy').value = questionsPerRound;
    document.getElementById('medium').value = 0;
    document.getElementById('hard').value = 0;

    // Makes the label display above the input
    document.getElementById('label_easy').className = 'active';
    document.getElementById('label_medium').className = 'active';
    document.getElementById('label_hard').className = 'active'
}

// Functions below are used to inject the Category choice dropdowns based on number of rounds selected
// The first extracts the data from the API
// The second injects the API dat and the code into html to dynamically create the dropsdowns
if(document.getElementById("rounds")) {
    document.getElementById("rounds").addEventListener("keyup", getCategoriesFn);
}

async function getCategoriesFn() {
    // Extracting the Categories from the API
    let url = `https://opentdb.com/api_category.php`;

    response = await fetch(url),
    json_categories = await response.json();
    let category_names = json_categories.trivia_categories;
    console.log(category_names);

    getRoundsDataFn(category_names);
}

async function getRoundsDataFn(category_names) {
    // Get the number of rounds entered by the User
    roundsPerGame = parseInt(document.getElementById('rounds').value);

    var text = "";
    var i = 1;
    
    while (i <= roundsPerGame) {
        let categoryName = null;
        if(document.getElementById(`cat-${i}`)) {
            categoryName = document.getElementById(`cat-${i}`).textContent;
        }
        text += `
        <div class="input-field col xs12 s6 l4">
            <div class="select-wrapper">
                <select id="round${i}" name="round${i}" style="display:block;" required>
                    <option class="cats_first" value="" disabled ${!categoryName && 'selected'}>Round ${i} Category</option>`
                    // For loop required below to extract each category name
                    for(let j = 0, len=category_names.length; j<len; j++ ){
                        // If category name in DB, it becomes "selected" and displays in Quiz Admin details
                        text += `<option value='${JSON.stringify(category_names[j])}' ${category_names[j]['name'] === categoryName && 'selected'}>${category_names[j]['name']}</option>`
                    }
        text += `</select>
            </div>
        </div>`;
        i++;
    }
    document.getElementById("categories_row").innerHTML = text;
}

// Quiz_Admin Details - Auto-adjust height of invitees textarea
// Source: https://stackoverflow.com/questions/995168/textarea-to-resize-based-on-content-length
function textAreaAdjust(element) {
  element.style.height = "1px";
  element.style.height = (25+element.scrollHeight)+"px";
}

// Function to allow Users to select an answer, deactivate the question block once a choice has...
//...been made, and highlight the correct answer. 
// Initial coding provided by Tutor/Mentor support to only make correct green and all incorrect red.
let roundScore;
let roundScoreInt;
$(".answer_button").on("click", function (event) {
    // only target $(this) specific round's score element/span
    roundScore = $(this).parent().parent(".collapsible-body").siblings(".center-align").children("h6").children("span[id^='correct-in-round-']")[0];
    // convert round's score (as integer)
    roundScoreInt = parseInt($(roundScore).text());
    if ($(this).hasClass("correct-answer")) {
        // Turns correct answer green
        $(this).addClass("green");
        if (isNaN(roundScoreInt)) {
            // change "Game not played yet" to integer 1 (first correct answer!)
            $(roundScore).text("1");
        } else {
            // otherwise, has previously had a correct answer, so already an integer
            roundScoreInt += 1;
            $(roundScore).text(roundScoreInt);
        }
    } else {
        // If user's answer was incorrect, turns it red
        $(this).addClass("red");
        // Highlight the actual correct on with green
        $(this).siblings(".correct-answer").addClass("green");
        // change "Game not played yet" to integer 0 (first click was incorrect!)
        if (isNaN(roundScoreInt)) {
            $(roundScore).text("0");
        }
    }
    // Prevents an answered question from being clicked again
    // Prevents quiz from being edited once it has started
    $(".answer_button_row").on("click", function () {
        $(this).css("pointer-events", "none");
        document.getElementById("details-form").style.pointerEvents = "none";
    });
});

// Function to count the scores by recording a value of 1 for each correct answer in Quiz Admin
let clicks = 0;
function addScoreFn(round) {
    // console.log(round);
    // clicks++;
    // document.getElementById(`count${round}`).innerHTML = clicks;
    // openModalFn(clicks); 
}





// Functions to display a modal with the total quiz scores
// From: https://www.w3schools.com/howto/howto_css_modals.asp
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];

function openModalFn(clicks) {
  modal.style.display = "block";
  document.getElementById('count2').innerHTML = clicks;
  console.log("Clicks: ")
};

span.onclick = function() {
  modal.style.display = "none";
};

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Function to display the waiting preloader
function preLoaderFn() {
    document.getElementById('preloader').style.display = "block";
};