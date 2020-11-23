# **Contents**
1 - [Introduction](#1-introduction)  
* 1.1 - [What is Mongo Quiz](#2-what-is-mongo-quiz)  
* 1.2 - [Background](#3-background)  
* 1.3 - [What Problem Does it Address?](#3-what-problem-does-it-address)  
* 1.4 - [How Does it Work?](#4-how-does-it-work) 

2 - [Site UI](#2-site-ui)  
* 2.1 - [Research](#2.1-research)  

3 - [Site Content](#3-site-content)  
* 3.1 - [Index Page](#3.1-index-page)  
* 3.2 - [About Page](#3.2-index-page)  
* 3.3 - [Register Page](#3.3-index-page)  
* 3.4 - [Login Page](#3.4-index-page)  
* 3.5 - [Profile Page](#3.5-index-page)  
* 3.6 - [Create a Quiz Page](#3.6-index-page)  
* 3.7 - [Quiz Admin Page](#3.7-index-page)  
* 3.8 - [Log Out](#3.8-index-page)  

4 - [Deployment](#4-deployment)
* 4.1 - [GitHub](#4.1-github)
* 4.2 - [Heroku](#4.2-heroku)  

5 - [Testing](#5-testing)
* 5.1 - [Testing File](#5.1-testing-file)
* 5.2 - [Known Bugs](#5.2-known-bugs)
* 5.3 - [Linting](#5.3-linting)

6 - [Technologies Employed](#6-technolgies-employed)

7 - [Acknowledgements](#6-Acknowledgements)
* 7.1 - [Universal](#6.1-universal)
* 7.2 - [Index Page](#6.2-index-page)  
* 7.3 - [About Page](#6.3-about-page)  
* 7.4 - [Register Page](#6.4-register-page)  
* 7.5 - [Login Page](#6.5-login-page)  
* 7.6 - [Profile Page](#6.6-profile-page)  
* 7.7 - [Create a Quiz Page](#6.7-create-a-quiz-page)  
* 7.8 - [Quiz Admin Page](#6.8-quiz-admin-page)  
* 7.9 - [Logout](#6.9-logout)  

8 - [Future Functionality](#7-future-functionality)

---
---

# **1 Introduction**  
[Back to Contents](#contents)  
Mongo Quiz is my third milestone project for the Code Institute "Full Stack Software Development Diploma".
It's principal purpose is to demonstrate my abilities and knowledge of working with and combining HTML, CSS,
Javascript and Python languages, while working with the Flask micro-framework and MongoDB database. 

## **1.1 What is Mongo Quiz**
It's an online pub-style quiz that can be played solo or with multiple players and teams. It comprises categorized
rounds of questions that are overseen by a quiz master who keeps a running total of all players' rounds scores.
The intention is for players to play at the same time while engaging with each other on a video platform such
as Zoom or Skype for maximum interaction and banter. The initial iteration is an MVP that provides a
minimal core level of functionality.

## **1.2 Background**
The Covid-19 lockdown saw most extended families unable to interact physically, instead moving their
communications online. One popular activity was the playing of quizzes. In my own case, we had one on
a weekly basis where the questions were read out and teams kept note of their scores. Each household 
produced one round of ten questions, thus passing the Quiz Master baton between rounds.

The activity was short-lived however, being played for only 5 or 6 weeks. The issue was that many family
members struggled to find time to collate questions, and even struggled coming up with a category each 
week. An additional problem was that questions being verbally called out could be difficult to hear at
times as a result of background noise or poor internet connection.

## **1.3 What Problem Does it Address**
Mongo Quiz offers several improvements on the method mentioned above:  
* **1 - Categories:** More than two dozen individual categories covering a broad range of subjects issue
available.
* **2 - Questions:** The questions database contains more than 26,000 choices.
* **3 - Convenience & Speed:** Creating a quiz is fast and uncomplicated. 
* **4 - Clarity:** Because all players can see the questions and potential answers onscreen, the problem
of not being able to hear questions is erradicated

## **1.4 How Does it Work**
A short "Create a Quiz" form allows Users to set a Quiz Name, decide the number of rounds and the category
for each, and the number of questions per round and the difficulty of each. Once copmpleted, the site 
connects with the <https://opentdb.com/api_config.php> API to populate the questions. Each request to the API for
questions is accompanied by a token that ensures questions are not repeated within the same quiz. **Note:**
the categories are also provided by way of an API call. It and the token generation are done separately 
and prior to the questions call.

At the time of creating the quiz, the owner provides the email addresses of anyone they expect to take
part. Once those players register, the quiz will be visible to them as email addresses are used as the
ID key to determine who can see what quizzes.

Players are given a choice of four answers for each question. Selecting a correct answer will add a
point to the Round and overall score. Correct answers are highlighted in green, with incorrect answers
showing in red when selected. Once a question has been answered, it cannot be changed.

At the end of each round players verbally submit their scores to the Quiz Master.

---
---

# **2 Site Design**  
[Back to Contents](#contents)  
The site is designed to be light in appearance, containing minimal of information. The functionality
is structured so that it is intuitive and easy to self-learn with only a bare skeleton of pages and
visuals on each. Because the site is primarily aimed at adults, the general look and feel to it is
one of maturity but fun.  

## **2.1 Colour Scheme**
The colour scheme comprises three complimentary colours each with unisex appeal:
- **Primary:** Aqua Green
- **Secondary:** Pink
- **Tertiary:** Navy

## **2.2 Imagery**
So as to keep the website uncluttered, only minimal visuals are employed. That is two images that
are positioned as backgrounds on each page. Fort added dynamicism, a parallax is applied to give 
the impression of additional movement on the page. 

The images choosen reflect the mature, but fun feel to the page while highlighting the fact that
this is a quiz website. The two images were sourced via Google and adapted for use on the site.

* **Pink Q Mark:** <https://storage.googleapis.com/pr-newsroom-wp/1/2019/05/Spotify-Quiz-Header.jpg>
* **Lightbulbs:** <https://blog.woobox.com/wp-content/uploads/8-Best-Quiz-Ideas-to-Entertain-Inform-Your-Audience-v1.png>


## **2.2 Typography**
Fonts on the site come from <https://fonts.google.com/>. The font choices was based on the desire
to use something clear and mature, while at the same time confirming the fun side of the website.
The choice made was baseed on guidance from this article by Inkbot Design:
<https://inkbotdesign.com/google-font-combinations-mixing-typefaces/>

* **Headings - Amatic:** <https://fonts.google.com/specimen/Amatic+SC?query=amatic+sc&sidebar.open=true&selection.family=Amatic+SC:wght@700|Josefin+Sans:ital@0;1>
* **Body Content - Josefin:** <https://fonts.google.com/specimen/Josefin+Sans?query=Josefin+Sans&sidebar.open=true&selection.family=Josefin+Sans:ital@0;1#standard-styles>

Icons are employed extensively throughout the site and are taken from <https://fontawesome.com/>

---
---

# **3 Site Content**  
[Back to Contents](#contents) 

## **3.1 Index Page**  
The Index or Home page is the page Users initially land out. The content is common to logged in and
non-logged in Users, the only difference being logged in Users see an additional button, "Create" that
is not shown to non-logged in Users. Both sets of Users can see the "More" button which navigates to
the About page.
* **Wireframes**  
-- [Desktop](static/images/wireframes/001_index_desktop.png)  
-- [Tablet](static/images/wireframes/001_index_tablet.png)  
-- [Mobile](static/images/wireframes/001_index_mobile.png)  

## **3.2 About Page**  
The About page gives visitors and Users alike a brief overview of what the website is and how it
should be used. It is seen an initial step to allow Users self-learn how the site works and is
best interacted with.

Non-logged in Users will be shown a Register button which takes them to the Register page. logged
in Users will be shown the Create button that takes them to the Create a Quiz page.
* **Wireframes**  
-- [Desktop](/images/wireframes/002_about_desktop.png)  
-- [Tablet](/images/wireframes/002_about_tablet.png)  
-- [Mobile](/images/wireframes/002_about_mobile.png)  

## **3.3 Register Page**  
The Register page allows visitors to register an account. As the site is fun based, minimial
sign-up information is required with Users being asked only to provide a:
- Player name  
- Email address (This is used as the primary key so an email can only be used for a single account) 
- Password  

To complete registration, User clicks the "Register" button. This aves the new data to the
database and navigates the User to their profile. Should they not wish to proceed, they can
click cancel or simply navigate away from the page.

* **Wireframes**  
-- [Desktop](/images/wireframes/003_register_desktop.png)  
-- [Tablet](/images/wireframes/003_register_tablet.png)  
-- [Mobile](/images/wireframes/003_register_mobile.png)  

## **3.4 Login Page**  
The Login page allows Users that already regsitered to access the site by providing their email
address and password. Once logged in they are brought to their Profile page. 
* **Wireframes**  
-- [Desktop](/images/wireframes/004_login_desktop.png)  
-- [Tablet](/images/wireframes/004_login_tablet.png)  
-- [Mobile](/images/wireframes/004_login_mobile.png)  

## **3.5 Profile Page**  
The Profile page serves two purposes. The first to give Users access to their personal information,
and the second to provide a central repository where all quizzes that they have created or invited
to participate in are displayed. This is done by way of a tabbed card (one for each quiz), that lists
the quiz basics and provides an Open button to allow the User view a specific quiz in its Quiz Admin
page.

The page also includes a "Create" button that brings the User to the Create a Quiz page, as well 
either a "Delete" or "Remove" button. The former is shown to the quiz owner. Clicking it deletes the
quiz from the database and all invited players profiles. If the User is not the Quiz owner, they see
a "Remove" button. Clicking it removes their participation in the Quiz by removing their email address
from the list of invitees of that quiz in the database. Clicking "Remove" doesn't affect any other
players. 
* **Wireframes**  
-- [Desktop](/images/wireframes/005_profile_desktop.png)  
-- [Tablet](/images/wireframes/005_profile_tablet.png)  
-- [Mobile](/images/wireframes/005_profile_mobile.png)  

## **3.6 Create a Quiz Page**  
The Create a Quiz page allows Users to create a new quiz. It consists of multiple fields, each of
which when saved adds an individual piece of data to the database. Each quiz has its own database
entry and a unique ID. The quiz fields and buttons are as below. Failure to complete a field
correctly or at all, will produce an error notification when the User tries to save the quiz.
* **Quiz Name***: USers give their quiz a name. It doesn't have to be unique
* **Rounds***: Allows the User to select the number of Rounds. Min 1, max 10
* **Categories***: These fields display once the User indicates the number of rounds. One drop
Dropdown displays for each round. The catagories are dynamcially populated from the API and a
Javascript function. API categories link is <https://opentdb.com/api_category.php>
* **Questions***: The User indicates the number of questions to be included per round. The same
quantity applies to all rounds. The number must be between 1 and 10. Whatever number is added
here, by default populates the "Easy" difficulty field.
* **Difficulty Fields***: The User can select the level of difficulty for the quiz questions by
indicating how many questions apply to each level. The combined total for all three fields must
match the Questions quantity. Where it doesn't the User will be notified. 
* **Players**: The only non-compulsory field allows the User to add the email addresses of the
persons they want to participate. They are added to the database as "invitees". A Users email
address mucty be included in order for them to view and participate in a game. Anyone whose
email address is included as an invitee, will have that quiz show up on their profile. The
Invitees on the database also includes the owner's email address as this is required for certain
functionality on the site.
* **Create Button**: Once the User has correctly completed all the necessary fields and they
click this button, the data is added to the database. 

* **Wireframes**  
-- [Desktop](/images/wireframes/006_create_desktop.png)  
-- [Tablet](/images/wireframes/006_create_tablet.png)  
-- [Mobile](/images/wireframes/006_create_mobile.png)  

## **3.7 Quiz Admin Page**  
**Rounds & Questions:** The Quiz Admin page is where Users play the game. Each quiz has a dedicated 
Admin page that includes a collapsible "Rounds" section where Users can see each round, its category, 
and the questions associated with each. The rounds are numbered sequentially, and each has its own
collapsible card.
* **Wireframes**  
-- [Desktop](/images/wireframes/007_quiz_admin_desktop.png)  
-- [Tablet](/images/wireframes/007_quiz_admin_tablet.png)  
-- [Mobile](/images/wireframes/007_quiz_admin_mobile.png)  

**Questions, Answers & Scores:** The questions are sequentially numbered and are accompanied by the
difficulty level and four possible answers. Where a User clicks the correct answer, it goes green and
all other answers do not change. Where the User clicks an incorrect answer, it goes red, the correct
one goes green, and the other two incorrect answers do not change.At the end of each round is a section
to display that round's score. It increments by one for each correct answer. Beneath all of the rounds,
the Total Quiz Score is displayed. It displays a running total for all rounds and questions answered. 
* **Wireframes**  
-- [Desktop](/images/wireframes/008_quiz_admin_rounds_desktop.png)  
-- [Tablet](/images/wireframes/008_quiz_admin_rounds_tablet.png)  
-- [Mobile](/images/wireframes/008_quiz_admin_rounds_mobile.png)  

**Quiz Details:** If the page has been accessed by the owner of the quiz, a "Details" section also
displays. This expandible card lists all of the QUiz details and player email addresses. The User
can change any of these details and click "Update" to update the quiz. Beneath the Details section
is a unique link that can be given to other players to bring them to the page to play the game 
(provided they are registered and logged in).
* **Wireframes**  
-- [Desktop](/images/wireframes/009_quiz_admin_details_desktop.png)  
-- [Tablet](/images/wireframes/009_quiz_admin_details_tablet.png)  
-- [Mobile](/images/wireframes/009_quiz_admin_details_mobile.png)  

## **3.8 Log Out**  
The Logout functionality is activated by clicking "Logout" in the navbar. This activates
a function that returns the User to the Login page.

---
---

# **4 Deployment**
[Back to Contents](#contents)  

## **4.1 GitHub**  
The repository for the code is GitHub and the code can be found at <https://github.com/CathalDolan/mongo-quiz>.
Owing to there being a single developer and due to the simplicity of the site, development was carried out
on a single master branch. However, going forward this will be changed to two; a development branch and and
master branch.

Each new piece of development was added, committed and pushed to GitHub via the terminal using the following
commands:
- $ git add -A / git add [file_name]
- $ git commit -m "Reason for commit"
- $ git push

To access the code from GitHub:
* 1 - Visit <https://github.com/CathalDolan/mongo-quiz>
* 2 - In the project repository above and click 'Code' button
* 3 - Copy the url (see https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository)
* 4 - From the Python Package Index (PyPI) repository install the following in the code editor:  
-- Git  
-- pip3  
-- dnspython  
-- flask  
-- flask-pymongo  
-- flask-wtf  
* 5 - Install the cloned repository by running the code obtained in points 1 to 3 above.
* 6 - Create a requirements.txt file by running: pip3 freeze --local > requirements.txt

## ** 4.2 MongoDb**
In MongoDb click on the connect button on the cluster to be connected.
* Choose the 2nd option, "connect your aspplication" and copy the connection string provided.
* Create an env.py file to contain the MONGO_URI connection string (the code just copied). 
* Correct the 'dbname' and 'password' values in the connection string to the correct values for Mongo Quiz.  
* Add the env.py file to .gitignore.
* Ensure env.py file contains:
-- import os  

-- os.environ.setdefault("IP", "0.0.0.0")  
-- os.environ.setdefault("PORT", "5000")  
-- os.environ.setdefault("SECRET_KEY", "secret key in Heroku Config Vars")  
-- os.environ.setdefault("MONGODB_DBNAME", "mongo-quiz")  
-- os.environ.setdefault("MONGO_URI", "mongodb+srv://database1:database1@myfirstcluster.aw8mt.mongodb.net/mongo-quiz?retryWrites=true&w=majority")  
* Save it and the program can be run locally by using the command: python3 run.py  

## **4.2 Heroku**
Merges to Heroku is done from the GitHub master branch. The site is deployed via Heroku
with the published version being visible on <https://mongo-quiz.herokuapp.com>. To keep
it up to date, each "push" to Github is automatically added to Heroku through settings
so any merges to the GitHub master branch are automatically deployed and built in Heroku.

## **4.2.1 - Connect to Heroku:**  
* Create a Procfile to initiate the Heroku web dyno using teh command. echo web: python3 run.py > Procfile  
* In your Heroku App, Settings click Reveal Config Vars.  
* Configure the variables to match those listed in the env.py file.  

## **4.2.2 - Deploy to Heroku from GitHub:**  
* Access the Deploy tab in Heroku.  
* For Deployment method, choose GitHub.  
* provide the repository name and GitHub password.  
* Click deploy from master branch.  
* This setting is currently automated so that new merges to the GitHub master branch automatically 
redeploy and build on Heroku Apps.  
 
---
---

# **5 Testing**
[Back to Contents](#contents)  

## **5.1 Testing Link**
The Testing suite is contained in a separate file: [Testing Doc](TESTING.md)

## **5.2 Known Bugs**  
- **Quiz Admin - Matching Round Categories:** Where a User chooses the same categories for different
rounds, each round will contain a set of questions for each category. For example, if a User selects
Art for two rounds, and each round has five questions, under each of the Art rounds, there will be a
total of ten questions, laid out in two sets of five.
- **Quiz Admin - Details Section Owner Email:** Certain functionality requires the quiz owners email
address to be included as an invitee. Because of this, when the quiz Details are viewed, the owners
email address is listed. If they delete it at this stage, they will lose access to the quiz. 
- **Quiz Admin - Categories Disappear if Difficulty isn't equal to Questions:** It is necessary for
the number of questions to equal the total for all three difficulty levels. Where this doesn't happen
a warning is displayed. However, this involves a refresh, and when done the previously chosen
categories are not retained, nor do the fields appear by default. 
- **Profile Page - No Quizzes Yet:** Where a User has neither created nor been invites to participate
in a quiz, the quizzes section on teh Profile page should state "No quizzes created yet". Although 
this functionality is in place, it is not functioning once there are any quizzes in the database.
- **Quiz Admin - Shared Quizzes Don't Match:** Where a player is invited to participate in a quiz
created by another player, the questions will not match as each player is making their iwn API call
for questions.

## **5.3 Linting**  
Each piece of code was put through a "checker" to review the quality of the code.  

### **5.3.1 HTML**  
* **Website:** <https://validator.w3.org/nu/#textarea>  
* **Result:** All code passed, primarily with the exception of lines containing Jinja2 code. 
An repeated ID error was also ignored because the line of code is added dynamically and only
one of the lines of code will be included.  

### **5.3.2 CSS**  
* **Website:** <https://jigsaw.w3.org/css-validator/validator>  
* **Result:** No errors or issues found  

### **5.3.3 JavaScript**  
* **Website:** <https://jslint.com/>  
* **Result:** Instances of "Double Quotes" ignored as a decision was made to use single quotes  

### **5.3.4 Python**  
* **Website:** <http://pep8online.com/>  
* **Results:** No errors or issues found  

---
---

# **6 Technolgies Employed**  
[Back to Contents](#contents)  

## **6.1 Materialize:** 
As much as possible, existing code from the Materialize framework was employed. It is accessed
via CDN. Set-up details as per <https://materializecss.com/getting-started.html>

## **6.2 Flask:** 
The Flask micro-framework forms the backbone of the functional code and is used in conjunction
with Python and Jinja2 in the HTML. <https://flask.palletsprojects.com/en/1.1.x/>

## **6.3 Python:** 
As much as possible, functionality was created using Python.

## **6.4 Javascript:** 
Where functions could not be created in Python, Javascript was used. On occasion this also called
for the use of JQuery. The latter is accessed bia CDN.

## **6.5 CSS:** 
The majority of styling of the HTML code is done with CSS, though certain Flask and Materialize
code has it's own inbuilt styling.

## **6.6 HTML:** 
Basic site layout and structure is achieved with HTML. However, in conjunction with Flask,
Jinja2 was extensively used: <https://jinja.palletsprojects.com/en/2.11.x/>.

---
---

# **7 Acknowledgements**  
[Back to Contents](#contents)  

## **7.1 Code Institute**
The tutoring and mentoring teams at Code Institute provided much guidance throughout the creation
of this project. Their assistance was required not only with bug fixing, but in helping to tease
out and develop code that was beyong my learnings

## **7.2 Other Third Parties**
One of the most valueable tools during development was Google as it allowed me to search for
answers and suggestions. It connected me with individuals and provided assistance via platforms
such as w3Schools, StackOverFlow and GeeksForGeeks to name a few.  

## **7.3 Pre-Written Code**
Certain pieces of code were copied from other creators and either used verbatim, or adapted to
meet the needs of the site. What follows is a page by page detail on what is used where.

### **7.3.1 Universal**  
"Universal" refers to elements that are either used across the entire site.  

* Parallax images in background: <https://materializecss.com/parallax.html>
* Position Navbar above the parallax image: <https://codepen.io/j_holtslander/pen/RVXzqm?html-preprocessor=pug>  
* Indicate active page on the Navbar: <https://stackoverflow.com/questions/18600031/changing-the-active-class-of-a-link-with-the-twitter-bootstrap-css-in-python-fla>  
* Side Navbar on mobile devices: <https://materializecss.com/mobile.html>
* Display Favicon: <https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/>  
* 404 page inclusion: <https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/>  
* Preloader displayed while waiting for an action to complete: <https://materializecss.com/preloader.html>  

### **7.3.2 Index Page**  
N/A  

### **7.3.3 About Page**  
N/A 

### **7.3.4 Register Page**  
* Email input pattern: <https://stackoverflow.com/questions/5601647/html5-email-input-pattern-attribute/36379040> (2nd answer)  
* Tooltips on input fields: <https://materializecss.com/tooltips.html>

### **7.3.5 Login Page**  
* Email input pattern: <https://stackoverflow.com/questions/5601647/html5-email-input-pattern-attribute/36379040> (2nd answer)  
* Tooltips on input fields: <https://materializecss.com/tooltips.html>

### **7.3.6 Profile Page** 
* Collapsible section to show quizzes:<https://materializecss.com/collapsible.html> 
* Sorting quiz tabs in Profile page to put most recent first: <https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2>    

### **7.3.7 Create a Quiz Page**  
* Dropdown "Select" menus: <https://materializecss.com/select.html>
* Input Fields: <https://materializecss.com/text-inputs.html>
* Tooltips on input fields: <https://materializecss.com/tooltips.html>

### **7.3.8 Quiz Admin Page**  
* Collapsible sections to show Rounds and Details: <https://materializecss.com/collapsible.html> 
* Dropdown "Select" menus: <https://materializecss.com/select.html>
* Input Fields: <https://materializecss.com/text-inputs.html>
* Autoadjust the height of invitees textarea in Details section: <https://stackoverflow.com/questions/995168/textarea-to-resize-based-on-content-length>  
* Shuffle quiz answers to randomize them - <https://note.nkmk.me/en/python-random-shuffle/>  
* Adding Scores Function - <https://stackoverflow.com/questions/20956138/how-to-add-1-to-a-javascript-variable-by-clicking-a-button>  
* Quiz Admin - Scores Modal <https://www.w3schools.com/howto/howto_css_modals.asp>  
* Jinja Variables: <https://jinja.palletsprojects.com/en/2.11.x/templates/#assignments>  
* Tooltips on input fields: <https://materializecss.com/tooltips.html>

### **7.3.9 Logout**  
N/A 

---
---

# **8 Future Functionality**  
[Back to Contents](#contents)  
Several improvements are envisioned to improve the user experience when interacting with Mong Quiz:
* **Player Edits:** Players will be able to edit their player details.
* **Password Functions:** Players will be able to request a lost password and/or reset and existing one.
* **Email Notifications:** Players will be invited to play via email sent directly from the site
* **QM Control Rounds & Questions:** The quiz master will be able to publish the rounds, as well as
the individual questions, one by one so that they display on teh players pages in real time.
* **All scores visible:** At the end of each round, all scores will be available to all players.
* **Scores Retained:** At the end of each game, each players scores will be added to and Retained
in the database so that they can be displayed on teh players profiles.
* **League Functionality:** Players will have the option to participate in a league where the Results
of multiple games are collated.

---
---