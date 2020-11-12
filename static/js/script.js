$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    
    $('#textarea1').val('');
    M.textareaAutoResize($('#textarea1'));
    
});

// Functions below are used to validate Difficulty qty matches Questions qty
// They couples with "if difficulty_total == quiz_details['questions']:" in def(create) in app.py
document.getElementById("questions").addEventListener("keyup", getQuestionsDataFn);

function getQuestionsDataFn() {
    questionsPerRound = parseInt(document.getElementById('questions').value);

    document.getElementById('easy').value = questionsPerRound;
    document.getElementById('medium').value = 0;
    document.getElementById('hard').value = 0;

    // Makes the label display above the input
    document.getElementById('label_easy').className = 'active';
    document.getElementById('label_medium').className = 'active';
    document.getElementById('label_hard').className = 'active';
};


// Functions below are used to inject the Category choice dropdowns based on number of rounds selected
// The first extracts the data from the API
// The second injects the API dat and the code into html to dynamically create the dropsdowns
document.getElementById("rounds").addEventListener("keyup", getCategoriesFn);

async function getCategoriesFn() {

    // Extracting the Categories from the API
    let url = `https://opentdb.com/api_category.php`;

    response = await fetch(url),
    json_categories = await response.json();
    let category_names = json_categories.trivia_categories;

    getRoundsDataFn(category_names);
}

async function getRoundsDataFn(category_names) {

    // Get the number of rounds entered by the User
    roundsPerGame = parseInt(document.getElementById('rounds').value);

    var text2 = "";
    for(let j = 0, len=category_names.length; j<len; j++ ){
        text2 += `
            <option value="${category_names[j]['name']}">${category_names[j]['name']}</option>
        `
    }

    var text = "";
    var i = 1;
    //For loop required below to populate each category name
    while (i <= roundsPerGame) {
        text += `
        <div class="input-field col xs12 s6 l4">
            <div class="select-wrapper">
                <select id="round${i}" name="round${i}" style="display:block;" required>
                    <option class="cats_first" value="" disabled selected>Round ${i} Category</option>
                    ${text2}
                </select>
            </div>
        </div>`;
        i++;
    }
    document.getElementById("categories_row").innerHTML = text;

}