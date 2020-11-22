# **Contents**
1 - [Introduction](#1-introduction)  
* 1.1 - [What is Mongo Quiz](#2-what-is-mongo-quiz)  
* 1.2 - [Background](#3-background)  
* 1.3 - [What Problem Does it Address?](#3-what-problem-does-it-address)  

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

6 - [Acknowledgements](#6-Acknowledgements)
* 6.1 - [Universal](#6.1-universal)
* 6.2 - [Index Page](#6.2-index-page)  
* 6.3 - [About Page](#6.3-about-page)  
* 6.4 - [Register Page](#6.4-register-page)  
* 6.5 - [Login Page](#6.5-login-page)  
* 6.6 - [Profile Page](#6.6-profile-page)  
* 6.7 - [Create a Quiz Page](#6.7-create-a-quiz-page)  
* 6.8 - [Quiz Admin Page](#6.8-quiz-admin-page)  
* 6.9 - [Logout](#6.9-logout)  

7 - [Future Functionality](#7-future-functionality)


# **1 Introduction**  
[Back to Contents](#contents)  
It's my MS project and designed to demonstrate proficiency in xyz. Inspired by personal experiences
during Covid-19 lockdown. MVP

## **1.1 What is Mongo Quiz**
[Back to Contents](#contents)  
It's a quiz that is designed to mimic the best parts of a traditional pub quiz.

## **1.2 Background**
[Back to Contents](#contents)  
Based on family quiz during lockdown.

## **1.3 What Problem Does it Address**
[Back to Contents](#contents)  
Based on family quiz during lockdown.


# **2 Site UI**  
[Back to Contents](#contents)  
It's my MS project and designed to demonstrate proficiency in xyz. Inspired by personal experiences
during Covid-19 lockdown.

## **2.1 Research**
[Back to Contents](#contents) 
## Typography, Layout, Colours  

## **2.2 Imagery**
Pink Q Mark - https://storage.googleapis.com/pr-newsroom-wp/1/2019/05/Spotify-Quiz-Header.jpg
lightbulbs - https://blog.woobox.com/wp-content/uploads/8-Best-Quiz-Ideas-to-Entertain-Inform-Your-Audience-v1.png
Icons: https://fontawesome.com/

## **2.2 Typography**
https://fonts.google.com/
Font choice based on needing a clear but light combo: https://inkbotdesign.com/google-font-combinations-mixing-typefaces/
Amatic for headings: https://fonts.google.com/specimen/Amatic+SC?query=amatic+sc&sidebar.open=true&selection.family=Amatic+SC:wght@700|Josefin+Sans:ital@0;1
Josefin for body: https://fonts.google.com/specimen/Josefin+Sans?query=Josefin+Sans&sidebar.open=true&selection.family=Josefin+Sans:ital@0;1#standard-styles


# **3 Site Content**  
[Back to Contents](#contents) 
The site is blah blah

## **3.1 Index Page**  
The Index or Home page, 

## **3.2 About Pag**  
The About page

## **3.3 Register Page**  
The Register page

## **3.4 Login Page**  
The Login page  

## **3.5 Profile Page**  
The Profile page 

## **3.6 Create a Quiz Page**  
The Create a Quiz page

## **3.7 Quiz Admin Page**  
The Quiz Admin page

## **3.8 Log Out**  
The Logout Functionality


# **4 Deployment**
[Back to Contents](#contents)  
## **4.1 GitHub**  
stuff and stuff  
## **4.2 Heroku**
Stuff and stuff  

# **5 Testing**
[Back to Contents](#contents)  

## **5.1 Texting Link**
The Testing suite is contained in a separate file: <TESTING.md>

## **5.2 Known Bugs**  
- Invitee quizes not working. Fixed with the if statements.  
- Home not working on mobile link - fixed with higher Z index  
- Question numbers - Fixed with materialize stuff.  
- Issue with text area - Fixed because calling wrong target you were calling #textarea1 instead of #invitees  
- Game Invite Link: https://stackoverflow.com/questions/18225302/how-can-i-wrap-or-break-long-text-word-in-a-fixed-width-span  

## **5.3 Linting**  
Each piece of code was put through a "checker" to review the quality of the code.  

### **5.3.1 HTML**  
* **Website:** https://validator.w3.org/nu/#textarea  
* **Result:** All code passed, primarily with the exception of lines containing Jinja2 code. 
An repeated ID error was also ignored because the line of code is added dynamically and only
one of the lines of code will be included.  

### **5.3.2 CSS**  
* **Website:** https://jigsaw.w3.org/css-validator/validator  
* **Result:** No errors or issues found  

### **5.3.3 JavaScript**  
* **Website:** https://jslint.com/  
* **Result:** Instances of "Double Quotes" ignored as a decision was made to use single quotes  

### **5.3.4 Python**  
* **Website:** http://pep8online.com/  
* **Results:** No errors or issues found  


# **6 Acknowledgements**  
[Back to Contents](#contents)  

## **6.1 Platforms, Third Parties & Languages Employed**

### **6.1.1 Materialize:** 
As much as possible, existing code from the Materialize framework was employed. It is accessed
via CDN. Set-up details as per https://materializecss.com/getting-started.html.

### **6.1.2 Flask:** 
The Flask micro-framework forms the backbone of the functional code and is used in conjunction
with Python and Jinja2 in teh HTML. https://flask.palletsprojects.com/en/1.1.x/.

### **6.1.3 Python:** 
As much as possible, functionality was created using Python

### **6.1.3 Javascript:** 
Where functions could not be created in Python, Javascript was used. On occasion this also called
for the use of JQuery. The latter is accessed bia CDN.

### **6.1.3 CSS:** 
The majority of styling of the HTML code is done with CSS, though certain Flask and Materialize
code has it's own inbuilt styling.

### **6.1.3 HTML:** 
Basic site layout and structure is achieved with HTML. However, in conjunction with FLask,
Jinja2 was extensively used: https://jinja.palletsprojects.com/en/2.11.x/

## **6.2 Universal**  
"Universal" refers to elements that are either used across the entire site.  

* Parallax images in background: https://materializecss.com/parallax.html
* Position Navbar above the parallax image: https://codepen.io/j_holtslander/pen/RVXzqm?html-preprocessor=pug  
* Indicate active page on the Navbar: https://stackoverflow.com/questions/18600031/changing-the-active-class-of-a-link-with-the-twitter-bootstrap-css-in-python-fla  
* Side Navbar on mobile devices: https://materializecss.com/mobile.html
* Display Favicon: https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/  
* 404 page inclusion: https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/  
* Preloader displayed while waiting for an action to complete: https://materializecss.com/preloader.html  

## **6.3 Index Page**  
N/A  

## **6.4 About Page**  
N/A 

## **6.5 Register Page**  
* Email input pattern: https://stackoverflow.com/questions/5601647/html5-email-input-pattern-attribute/36379040 (2nd answer)  
* Tooltips on input fields: https://materializecss.com/tooltips.html

## **6.6 Login Page**  
* Email input pattern: https://stackoverflow.com/questions/5601647/html5-email-input-pattern-attribute/36379040 (2nd answer)  
* Tooltips on input fields: https://materializecss.com/tooltips.html

## **6.7 Profile Page** 
* Collapsible section to show quizzes: https://materializecss.com/collapsible.html 
* Sorting quiz tabs in Profile page to put most recent first: https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2    

## **6.8 Create a Quiz Page**  
* Dropdown "Select" menus: https://materializecss.com/select.html
* Input Fields: https://materializecss.com/text-inputs.html
* Tooltips on input fields: https://materializecss.com/tooltips.html

## **6.9 Quiz Admin Page**  
* Collapsible sections to show Rounds and Details: https://materializecss.com/collapsible.html 
* Dropdown "Select" menus: https://materializecss.com/select.html
* Input Fields: https://materializecss.com/text-inputs.html
* Autoadjust the height of invitees textarea in Details section: https://stackoverflow.com/questions/995168/textarea-to-resize-based-on-content-length  
* Shuffle quiz answers to randomize them - https://note.nkmk.me/en/python-random-shuffle/  
* Adding Scores Function - https://stackoverflow.com/questions/20956138/how-to-add-1-to-a-javascript-variable-by-clicking-a-button  
* Quiz Admin - Scores Modal https://www.w3schools.com/howto/howto_css_modals.asp  
* Jinja Variables: https://jinja.palletsprojects.com/en/2.11.x/templates/#assignments  
* Tooltips on input fields: https://materializecss.com/tooltips.html

## **6.10 Logout**  
N/A 


# **7 Future Functionality**  
[Back to Contents](#contents)  
Stuff abnout the future