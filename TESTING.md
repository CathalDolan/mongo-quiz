# **Contents**
1 - [Universal](#1-universal)
- 1.1 - [Navbar](#1.1-navbar)
- 1.2 - [Footer](#1.2-footer)

2 - [Logged Out User](#2-logged-out-user)
- 2.1 - [Navbar](#2.1-navbar-(logged-out-user))
- 2.2 - [Index/Home Page](#2.2-index-page-(logged-out-user))
- 2.3 - [About Page](#2.3-about-page-(logged-out-user))
- 2.4 - [Register Page](2.4-register-page)

3 - [Logged In User](#3-logged-in-user)
- 3.1 - [Navbar](#3.1-navbar-(logged-out-user))
- 3.2 - [Index/Home Page](#3.2-index-page-(logged-out-user))
- 3.3 - [About Page](#3.3-about-page-(logged-out-user))
- 3.4 - [Profile Page](#3.4-profile-page)
- 3.5 - [Create a Quiz](#3.5-create-a-quiz)  
- 3.6 - [Quiz Admin - Quiz Owner](#3.6-create-a-quiz)  
- 3.7 - [Quiz Admin - Player](#3.7-create-a-quiz) 

# **Writers Note** 
I recognize that in a real world situation, a testing suite is required for all device types and sizes.
However, as the nuances between each are relatively small, for the purpose of avoiding extensive
repetition, the testing instructions that follow, are taken from the point of view of desktop testing.
The exception to this being the inital "Universal" section. 

# **1 Universal**  
[Back to Contents](#contents)

Universal elements affect all pages of the website and apply regardless of whether the User is logged
in or not.

## **1.1 Navbar**  
* 1 - On PC is the navbar shown as a series of links?  
**Desired Result:** Yes  
* 2 - On a Tablet is the navbar shown as a hamburger icon?  
**Desired Result:** Yes  
* 3 - On a Tablet does clicking the hamburger icon open the menu?  
**Desired Result:** Yes  
* 4 - On a Mobile is the navbar shown as a hamburger icon?  
**Desired Result:** Yes  
* 5 - On a Mobile does clicking the hamburger icon open the menu?  
**Desired Result:** Yes  

## **1.2 Footer**
* 1 - Is the footer present at the bottom of the page?  
**Desired Result:** Yes  
* 2 - Is the "About" link present?  
**Desired Result:** Yes  
* 3 - Test: Does "About" link bring User to About page?  
**Desired Result:** Yes  

# **2 Logged Out User**
[Back to Contents](#contents)
## **2.1 Navbar** (Logged Out User)
* 1 - When a User is logged out are the following four nav links displayed?  
** Home  
** About  
** Register  
** Login  
** **Desired Result:** Yes  

* 2 - Does "Home" link bring User to Home/Index page?  
**Desired Result:** Yes  
* 3 - Does "About" link bring User to About page?  
**Desired Result:** Yes  
* 4 - Does "Register" link bring User to Register page?  
**Desired Result:** Yes  
* 5 - Does "Login" link bring User to Login page?  
**Desired Result:** Yes  

## **2.2 Index Page** (Logged Out User)  
* 1 - If the User is logged out, does the "More" button display centred at the bottom of the page?  
**Desired Result:** Yes  
* 2 - Does clicking the "More" button take the User to the "About" page?  
**Desired Result:** Yes  

## **2.3 About Page** (Logged Out User)
* 1 - If the User is logged out, does the "Register" button display centred at the bottom of the page?  
**Desired Result:** Yes  
* 2 - Does clicking the "Register" button take the User to the "Register" page?  
**Desired Result:** Yes  

## **2.4 Register Page**
### **2.4.1 - Player/Team Name Field** (Register Page)
* 1 - Is the Player/Team Name field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Player/Team Name field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Player/Team Name field is left blank, does a notification display when the "Register" button is clicked?  
**Desired Result:** Yes  
* 4 - Does a notification display on the the Player/Team Name field if less than 5 characters are entered and the User clicks the "Register" button?  
**Desired Result:** Yes  
* 5 - Does the Player/Team Name field accept a maximum of 25 charcters and stop accepting characters if more than 25 are added?  
**Desired Result:** Yes  

### **2.4.2 - Email Field** (Register Page)
* 1 - Is the Email field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Email field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Email field is left blank, does a notification display when the "Register" button is clicked?  
**Desired Result:** Yes  
* 4 - Does a notification display on the the Email field if the address doesn't contain a minimum of 2 letters in each section, the @ symbol and a fullstop ( eg xx@yy.zz)?  
**Desired Result:** Yes  

### **2.4.3 - Password Field** (Register Page)
* 1 - Is the Password field present?
**Desired Result:** Yes 
* 2 - Does clicking the Password field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Password field is left blank, does a notification display when the "Register" button is clicked?  
**Desired Result:** Yes  
* 4 - Does a notification display on the the Password field if less than 5 characters are entered and the User clicks the "Register" button?  
**Desired Result:** Yes  
* 5 - Does a notification display on the the Password field if the password entered doesn't include at least one Uppercase and one Lowercase letter?  
**Desired Result:** Yes  

### **2.4.4 - Register Button** (Register Page)
* 1 - Is the "Register" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Register" button bring the User to their Profile page?  
**Desired Result:** Yes  
* 3 - When brought to the Profile page, does a "registered" confirmation display?  
**Desired Result:** Yes
* 4 - When the "Register" button is clicked, does it save the Username to the database?  
**Desired Result:** Yes  
* 5 - When the "Register" button is clicked, does it save the Email to the database?  
**Desired Result:** Yes 
* 6 - When the "Register" button is clicked, does it save the Password to the database?  
**Desired Result:** Yes  
* 7 - When the Password is saved to the database, is it hashed?  
**Desired Result:** Yes 

### **2.4.5 - Cancel Button** (Register Page)
* 1 - Is the "Cancel" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Cancel" button bring the User to the Home page?  
**Desired Result:** Yes  
* 3 - Does clicking the "Cancel" button save any data to the database?  
**Desired Result:** No  

### **2.4.6 - Links** (Register Page)
* 1 - Is the "Login" link present beneath the buttons?  
**Desired Result:** Yes  
* 2 - Does clicking the "Login" link bring the User to the Login page?  
**Desired Result:** Yes

## **2.5 Login Page**

### **2.5.1 - Email Field** (Login Page)
* 1 - Is the Email field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Email field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Email field is left blank, does a notification display when the "Register" button is clicked?  
**Desired Result:** Yes  
* 4 - Does a notification display on the the Email field if the address doesn't contain a minimum of 2 letters in each section, the @ symbol and a fullstop ( eg xx@yy.zz)?  
**Desired Result:** Yes  

### **2.5.2 - Password Field** Login Page)
* 1 - Is the Password field present?
**Desired Result:** Yes 
* 2 - Does clicking the Password field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Password field is left blank, does a notification display when the "Register" button is clicked?  
**Desired Result:** Yes  
* 4 - Does a notification display on the the Password field if less than 5 characters are entered and the User clicks the "Register" button?  
**Desired Result:** Yes  
* 5 - Does a notification display on the the Password field if the password entered doesn't include at least one Uppercase and one Lowercase letter?  
**Desired Result:** Yes  

### **2.5.3 - Login Button** (Login Page)
* 1 - Is the "Login" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Login" button bring the User to their Profile page if the correct email and password have been entered?  
**Desired Result:** Yes  
* 3 - Does clicking the "Login" button add a Session Cookie if the correct email and password have been entered?  
**Desired Result:** Yes  
* 4 - If the User enters an incorrect password, does a "wrong password or email" notification display?  
**Desired Result:** Yes  
* 5 - If the User enters an incorrect email, does a "wrong password or email" notification display?  
**Desired Result:** Yes  

### **2.4.5 - Cancel Button** (Login Page)
* 1 - Is the "Cancel" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Cancel" button bring the User to the Home page?  
**Desired Result:** Yes  
* 3 - Does clicking the "Cancel" button save any data to the database?  
**Desired Result:** No  

### **2.4.6 - Links** (Login Page)
* 1 - Is the "Register" link present beneath the buttons?  
**Desired Result:** Yes  
* 2 - Does clicking the "Register" link bring the User to the Register page?  
**Desired Result:** Yes

# **3 Logged In User**
[Back to Contents](#contents)  
## **3.1 Navbar** (Logged In User)
* 1 - When a User is logged out are the following five nav links displayed?  
** Home  
** About  
** Create a Quiz  
** Profile  
** Logout  
** **Desired Result:** Yes  

* 2 - Does "Home" link bring User to Home/Index page?  
**Desired Result:** Yes  
* 3 - Does "About" link bring User to About page?  
**Desired Result:** Yes  
* 4 - Does "Create a Quiz" link bring User to Create a Quiz page?  
**Desired Result:** Yes  
* 5 - Does "Profile" link bring User to Profile page?  
**Desired Result:** Yes  
* 6 - Does "Logout" link bring User to Logged Out Home page?  
**Desired Result:** Yes  
* 7 - Does clicking the "Logout" link remove all relevant data from the database?  
**Desired Result:** Yes 

## **3.2 Index Page (Logged In User)**  
* 1 - If the User is logged in, does the "More" button display bottom left of the page?  
**Desired Result:** Yes  
* 2 - Does clicking the "More" button take the User to the About page?  
**Desired Result:** Yes  
* 3 - If the User is logged in, does the "Create" button display bottom right of the page?  
**Desired Result:** Yes  
* 4 - Does clicking the "Create" button take the User to the Create a Quiz page?  
**Desired Result:** Yes  

## **3.3 About Page (Logged In User)**
* 1 - If the User is logged out, does the "Create" button display centred at the bottom of the page?  
**Desired Result:** Yes  
* 2 - Does clicking the "Create" button take the User to the "Create a Quiz" page?  
**Desired Result:** Yes 

## **3.4 Profile Page**
### **3.4.1 - Top Section**  
* 1 - Does the top of the page display "Hi Player/Team Name"?  
**Desired Result:** Yes  
* 2 - Is the team name displayed?  
**Desired Result:** Yes 
* 3 - Is it the correct team name?  
**Desired Result:** Yes 
* 3 - Is the email address displayed?  
**Desired Result:** Yes 
* 4 - Is it the correct email?  
**Desired Result:** Yes  
* 5 - Is the "Create" button displayed?  
**Desired Result:** Yes  
* 6 - Does clicking the "Create" button bring the USer to the Create a Quiz page?  
**Desired Result:** Yes  

### **3.4.2 - Quizzes Section (No Quizzes Shown)**
* 1 - If there are no quizzes displayed, are the tabs empty and uncoloured?
**Desired Result:** Yes 
* 2 - If there are no quizzes displayed, does the card mention "No quizzes created yet"?
**Desired Result:** Yes 

### **3.4.3 - Quizzes Section (Quizzes Included)**
[Back to Contents](#contents)  
* 1 - Does the tab include the Quiz name?  
**Desired Result:** Yes  
* 2 - If there are multiple quizzes, does clicking the tab open the appropriate card beneath?  
**Desired Result:** Yes   
* 3 - If there are more quizzes than there is space for tabs, does the scrollbar appear on PC?  
**Desired Result:** Yes  
* 4 - If there are more quizzes than there is space for tabs, can Users scroll on mobile?   
**Desired Result:** Yes  
* 5 - Is the quiz name displayed?  
**Desired Result:** Yes  
* 6 - Is the name of the Quiz Master displayed?  
**Desired Result:** Yes  
* 7 - Is the created date shown?  
**Desired Result:** Yes  
* 8 - Is the created date correct?  
**Desired Result:** Yes  

### **3.4.4 - Open Button**
* 1 - Is the "Open" button displayed?  
**Desired Result:** Yes  
* 2 - Does clicking the "Open" button bring the User to the Quiz Admin page?  
**Desired Result:** Yes  
* 3 - Does clicking the "Open" button display a waiting spinner?  
**Desired Result:** Yes  
* 4 - Does clicking the "Open" button bring the User to the correct Quiz Admin page?  
**Desired Result:** Yes  

### **3.4.5 - Delete Button**
* 1 - If the User is the Quiz Owner, is the "Delete" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Delete" remove the quiz from the tab?   
**Desired Result:** Yes  
* 3 - Does clicking the "Delete" remove the quiz data from the database?  
**Desired Result:** Yes  

### **3.4.6 - Remove Button**
* 1 - If the User is not the Quiz Owner, is the "Remove" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Remove" remove the quiz from the tab?   
**Desired Result:** Yes  
* 3 - Does clicking the "Remove" remove their email address from that quiz data in the database?  
**Desired Result:** Yes  
* 4 - Does clicking the "Remove" keep the quiz displayed on other players profiles?  
**Desired Result:** Yes  

## **3.5 Create a Quiz**
### **3.5.1 - Quiz Name Field** (Create a Quiz Page)
* 1 - Is the Quiz Name field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Quiz Name field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Quiz Name field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 4 - Does a notification display on the the Quiz Name field if less than 5 characters are entered and the User clicks the "Create" button?  
**Desired Result:** Yes  
* 5 - Does the Quiz Name field accept a maximum of 20 charcters and stop accepting characters if more than 25 are added?  
**Desired Result:** Yes  

### **3.5.2 - Rounds Field** (Create a Quiz Page) 
* 1 - Is the Rounds field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Rounds field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Rounds field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 4 - Does the field accept numerical characters only?  
**Desired Result:** Yes  
* 5 - If a number greater than 10 is entered, does a notification displaye when the "Create" button is clicked?  
**Desired Result:** Yes  
* 6 - When a number is entered, do a corresponding number of Category fields display beneath, left to right?  
**Desired Result:** Yes  

### **3.5.3 - Category Field(s)** (Create a Quiz Page)   
* 1 - If any category field(s) is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 2 - Does each dropdown include a choice of categories?  
**Desired Result:** Yes  
* 3 - Can the User scroll the entire amount?  
**Desired Result:** Yes  
* 4 - Is the User's choice displayed once selected?  
**Desired Result:** Yes  

### **3.5.4 - Questions Field** (Create a Quiz Page) 
* 1 - Is the Questions field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Questions field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Questions field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 4 - Does the field accept numerical characters only?  
**Desired Result:** Yes  
* 5 - If a number greater than 10 is entered, does a notification displaye when the "Create" button is clicked?  
**Desired Result:** Yes  
* 6 - When a number is entered, do a matching number display in the "Easy" difficulty field?  
**Desired Result:** Yes  
* 7 - When a number is entered, does a zero display in the "Medium" difficulty field?  
**Desired Result:** Yes  
* 8 - When a number is entered, does a zero display in the "Hard" difficulty field?  
**Desired Result:** Yes 

### **3.5.5 - Difficulty Fields** (Create a Quiz Page) 
* 1 - Is the Easy difficulty field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Easy difficulty  field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Easy difficulty  field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 4 - Does the Easy difficulty field accept numerical characters only?  
**Desired Result:** Yes
* 5 - Is the Medium difficulty field present?  
**Desired Result:** Yes  
* 6 - Does clicking the Medium difficulty  field icon show a tooltip?  
**Desired Result:** Yes  
* 7 - If the Medium field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 8 - Does the Medium difficulty field accept numerical characters only?  
**Desired Result:** Yes
* 9 - Is the Hard difficulty field present?  
**Desired Result:** Yes  
* 10 - Does clicking the Hard difficulty  field icon show a tooltip?  
**Desired Result:** Yes  
* 11 - If the Hard difficulty  field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 12 - Does the Hard difficulty field accept numerical characters only?  
**Desired Result:** Yes  
* 13 - If the total for all three fields is less than the Questions field quantity, does a flash message show when the "Create" button is clicked?  
**Desired Result:** Yes  
* 14 - If the total for all three fields is more than the Questions field quantity, does a flash message show when the "Create" button is clicked?  
**Desired Result:** Yes  
* 15 - If the total for all three fields is more than the Questions field quantity, do the already filled fields retain their data after the "Create" button is clicked?  
**Desired Result:** Yes  

### **3.5.6 - Players Field** (Create a Quiz Page)  
[Back to Contents](#contents)  
* 1 - Is the Players field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Players field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - If the Players field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  

### **3.5.7 - Create Button** (Create a Quiz Page)
* 1 - Is the "Create" button present on the bottom left?  
**Desired Result:** Yes  
* 2 - Does clicking the "Create" button bring the User to the Quiz Admin page (if all fields correctly completed)?  
**Desired Result:** Yes  
* 3 - Does clicking the "Create" button display a waiting spinner?  
**Desired Result:** Yes  
* 4 - When brought to the Quiz Admin page, does a "Quiz Sucessfully Created" confirmation flash display?  
**Desired Result:** Yes
* 5 - When the "Create" button is clicked, does it save the Quiz Name to the database?  
**Desired Result:** Yes  
* 6 - When the "Create" button is clicked, does it save the number of Rounds to the database?  
**Desired Result:** Yes  
* 7 - When the "Create" button is clicked, does it save the Categories to the database as an array with key values of ID and Name?  
**Desired Result:** Yes  
* 8 - When the "Create" button is clicked, does it save the number of Questions to the database?  
**Desired Result:** Yes  
* 9 - When the "Create" button is clicked, does it save all three Difficulty levels to the same field in the database as an array with key values of Name and Number?  
**Desired Result:** Yes  
* 10 - When the "Create" button is clicked, does it save the Players email addresses to the database?  
**Desired Result:** Yes  
* 11 - When the "Create" button is clicked, is the Quiz owners email added to the invitees list to the database?  
**Desired Result:** Yes  
* 12 - When the "Create" button is clicked, does it save the quiz owners Username to quiz the database?  
**Desired Result:** Yes  
* 13 - When the "Create" button is clicked, does it save the Created Date to quiz the database?  
**Desired Result:** Yes  

### **3.5.8 - Cancel Button** (Create a Quiz Page)
* 1 - Is the "Cancel" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Cancel" button bring the User to their Profile page?  
**Desired Result:** Yes  
* 3 - Does clicking the "Cancel" button save any data to the database?  
**Desired Result:** No  

## **3.6 Quiz Admin - Quiz Owner**  
[Back to Contents](#contents)  
### **3.6.1 - Page Top & Tail**
* 1 - Is the quiz name displayed at the top of the page?  
**Desired Result:** Yes  
* 2 - Is the Quiz Link section included?  
**Desired Result:** Yes  
* 3 - Does the Quiz quiz ID in the link match that in the page url?  
**Desired Result:** Yes  

### **3.6.2 - Rounds Collapsible**
* 1 - Is the Rounds section displayed?  
**Desired Result:** Yes  
* 2 - Are the individual Rounds collapsible card expanded by default?  
**Desired Result:** Yes  
* 3 - Does clicking the header collapse the card section beneath if expanded?  
**Desired Result:** Yes  
* 4 - Does clicking the header expand the card section beneath if collapsed?  
**Desired Result:** Yes  
* 5 - Do the number of Rounds heading displayed match the number the User selected when creating the quiz?  
**Desired Result:** Yes  
* 6 - Do the individual categories shown in the heading of each round match those selected when creating the quiz?  
**Desired Result:** Yes 
* 7 - Is the Round Score displayed at the end of the card?  
**Desired Result:** Yes  
* 8 - Prior to the game being started, does the round score state something like "game not started"?  
**Desired Result:** Yes  

### **3.6.3 - Individual Round Collapsible**
* 1 - Does clicking on a round header expand the card beneath if collapsed?  
**Desired Result:** Yes  
* 2 - Does clicking on a round header collapse the card beneath if expanded?  
**Desired Result:** Yes  
* 3 - Does the number of questioned displayed match the number slected by the User when the quiz was created?  
**Desired Result:** Yes  
* 4 - Do the questions match the category listed for the round?  
**Desired Result:** Yes  
* 5 - Is each question listed one beneath the other?  
**Desired Result:** Yes  
* 6 - Is each question numbered sequentially?  
**Desired Result:** Yes  
* 7 - Is the difficulty for each question shown?  
**Desired Result:** Yes  
* 8 - Do the quantity of questions for each difficulty match the choices made when the quiz was created?  
**Desired Result:** Yes  
* 9 - Does clicking on an incorrect answer turn that answer red?  
**Desired Result:** Yes  
* 10 - Does clicking on an incorrect answer turn the correct answer green?  
**Desired Result:** Yes  
* 11 - Does clicking on an incorrect answer have no affect on the other two incorrect answers?  
**Desired Result:** Yes  
* 12 - Does clicking on an incorrect answer add one to the score?  
**Desired Result:** No  
* 13 - Does clicking on the correct answer turn that answer green?  
**Desired Result:** Yes  
* 14 - Does clicking on the correct answer have no affect on the incorrect answers?  
**Desired Result:** Yes  
* 15 - Does clicking on the correct answer add one to the score?  
**Desired Result:** Yes  
* 16 - Does clicking on the correct answer display a modal stating the total score?  
**Desired Result:** Yes  
* 17 - Does clicking the X on the corect score modal close the modal?  
**Desired Result:** Yes  
* 18 - Does clicking on the modal side area close the modal?  
**Desired Result:** Yes  
* 16 - Once a question has been selected, can it or any of the questions in that block be clicked on?  
**Desired Result:** No
* 17 - Does the Round Score reflect the number of questions answered correctly in the round?  

### **3.6.4 - Total Quiz Score Section**
* 1 - Is the Total Quiz Score section displayed beneath the Rounds section?  
**Desired Result:** Yes  
* 2 - Prior to the game being started, does the Total Quiz Score state something like "game not started"?  
**Desired Result:** Yes 
* 3 - Does the Total Quiz Score reflect the total for all questions answered and rounds played?
**Desired Result:** Yes 

### **3.6.5 - Details Collapsible**
### **3.6.5.1 - Quiz Name Field** (Quiz Admin Page)
* 1 - Is the Quiz Name field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Quiz Name field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - Is the Quiz Name field prepopulated with the data from the Create a Quiz form?  
**Desired Result:** Yes  
* 4 - If the Quiz Name field is left blank, does a notification display when the "Update" button is clicked?  
**Desired Result:** Yes  
* 5 - Does a notification display on the the Quiz Name field if less than 5 characters are entered and the User clicks the "Update" button?  
**Desired Result:** Yes  
* 6 - Does the Quiz Name field accept a maximum of 20 charcters and stop accepting characters if more than 25 are added?  
**Desired Result:** Yes  

### **3.6.5.2 - Rounds Field** (Quiz Admin Page)
* 1 - Is the Rounds field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Rounds field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - Is the Rounds field prepopulated with the quantity from the Create a Quiz form?  
**Desired Result:** Yes  
* 4 - If the Rounds field is left blank, does a notification display when the "Update" button is clicked?  
**Desired Result:** Yes  
* 5 - Does the field accept numerical characters only?  
**Desired Result:** Yes  
* 6 - If a number greater than 10 is entered, does a notification displaye when the "Update" button is clicked?  
**Desired Result:** Yes  
* 7 - When a number is entered, do a corresponding number of Category fields display beneath, left to right?  
**Desired Result:** Yes  

### **3.6.5.3 - Category Field(s)** (Quiz Admin Page)   
* 1 - Are the category fields displayed, with the quantity matching the number of Rounds?  
**Desired Result:** Yes  
* 2 - Are the Category fields prepopulated with the choices from the Create a Quiz form?  
**Desired Result:** Yes  
* 3 - If any category field(s) is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 4 - Does each dropdown include a choice of categories?  
**Desired Result:** Yes  
* 5 - Can the User scroll the entire amount?  
**Desired Result:** Yes  
* 6 - Is the User's choice displayed once selected?  
**Desired Result:** Yes  

### **3.6.5.4 - Questions Field**  (Quiz Admin Page) 
* 1 - Is the Questions field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Questions field icon show a tooltip?  
**Desired Result:** Yes  
* 3 - Is the Questions field prepopulated with the quantity from the Create a Quiz form?  
**Desired Result:** Yes  
* 4 - If the Questions field is left blank, does a notification display when the "Update" button is clicked?  
**Desired Result:** Yes  
* 5 - Does the field accept numerical characters only?  
**Desired Result:** Yes  
* 6 - If a number greater than 10 is entered, does a notification display when the "Update" button is clicked?  
**Desired Result:** Yes  
* 7 - When a number is entered, does a matching number display in the "Easy" difficulty field?  
**Desired Result:** Yes  
* 8 - When a number is entered, does a zero display in the "Medium" difficulty field?  
**Desired Result:** Yes  
* 9 - When a number is entered, does a zero display in the "Hard" difficulty field?  
**Desired Result:** Yes 

### **3.6.5.5 - Difficulty Fields**  (Quiz Admin Page) 
* 1 - Is the Easy difficulty field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Easy difficulty  field icon show a tooltip?  
**Desired Result:** Yes  
* 4 - Is the Easy difficulty field prepopulated with the quantity from the Create a Quiz form?  
**Desired Result:** Yes  
* 5 - If the Easy difficulty  field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 6 - Does the Easy difficulty field accept numerical characters only?  
**Desired Result:** Yes
* 7 - Is the Medium difficulty field present?  
**Desired Result:** Yes  
* 8 - Does clicking the Medium difficulty  field icon show a tooltip?  
**Desired Result:** Yes  
* 9 - Is the Medium difficulty field prepopulated with the quantity from the Create a Quiz form?  
**Desired Result:** Yes 
* 10 - If the Medium field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 11 - Does the Medium difficulty field accept numerical characters only?  
**Desired Result:** Yes
* 12 - Is the Hard difficulty field present?  
**Desired Result:** Yes  
* 13 - Does clicking the Hard difficulty  field icon show a tooltip?  
**Desired Result:** Yes  
* 14 - Is the Hard difficulty field prepopulated with the quantity from the Create a Quiz form?  
**Desired Result:** Yes 
* 15 - If the Hard difficulty  field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  
* 16 - Does the Hard difficulty field accept numerical characters only?  
**Desired Result:** Yes  
* 17 - If the total for all three fields is less than the Questions field quantity, does a flash message show when the "Create" button is clicked?  
**Desired Result:** Yes  
* 18 - If the total for all three fields is more than the Questions field quantity, does a flash message show when the "Create" button is clicked?  
**Desired Result:** Yes  
* 19 - If the total for all three fields is more than the Questions field quantity, do the already filled fields retain their data after the "Create" button is clicked?  
**Desired Result:** Yes  

### **3.6.5.6 - Players Field** (Quiz Admin Page)  
[Back to Contents](#contents)  
* 1 - Is the Players field present?  
**Desired Result:** Yes  
* 2 - Does clicking the Players field icon show a tooltip?  
**Desired Result:** Yes  
* 4 - Is the Players field prepopulated with the addresses from the Create a Quiz form?  
**Desired Result:** Yes  
* 3 - If the Players field is left blank, does a notification display when the "Create" button is clicked?  
**Desired Result:** Yes  

### **3.6.5.7 - Update Button** (Quiz Admin Page)
* 1 - Is the "Update" button present on the bottom left?  
**Desired Result:** Yes  
* 2 - Does clicking the "Update" button refresh the page (if all fields correctly completed)?  
**Desired Result:** Yes  
* 3 - Does clicking the "Update" button display a waiting spinner?  
**Desired Result:** Yes  
* 4 - When the page refreshes, does a "Quiz Sucessfully Updated" confirmation flash display?  
**Desired Result:** Yes
* 5 - When the "Update" button is clicked, does it update the Quiz Name in the database if changed?  
**Desired Result:** Yes  
* 6 - When the "Create" button is clicked, does it update the Rounds in the database if changed?  
**Desired Result:** Yes  
* 7 - When the "Create" button is clicked, does it update the Categories in the database if changed?  
**Desired Result:** Yes  
* 8 - When the "Create" button is clicked, does it update the Number of Questions in the database if changed?  
**Desired Result:** Yes  
* 9 - When the "Create" button is clicked, does it update the difficulty levels in the database if changed?  
**Desired Result:** Yes  
* 10 - When the "Create" button is clicked, does it update the Players email addresses in the database if changed?  
**Desired Result:** Yes   

### **3.6.5.8 - Cancel Button** (Quiz Admin Page)
* 1 - Is the "Cancel" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Cancel" button bring the User to their Profile page?  
**Desired Result:** Yes  
* 3 - Does clicking the "Cancel" button update any data in the database?  
**Desired Result:** No  

### **3.6.6 - All Quizzes Button**
* 1 - Is the "All Quizzes" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "All Quizzes" bring the User to their profile page?  
**Desired Result:** Yes  

### **3.6.7 - Delete Button**
* 1 - Is the "Delete" button present?  
**Desired Result:** Yes  
* 2 - Does clicking the "Delete" bring the User to their profile page?  
**Desired Result:** Yes  
* 3 - Does clicking the "Delete" remove the quiz data from the database?  
**Desired Result:** Yes  

## **3.7 Quiz Admin - Player**  
[Back to Contents](#contents)  
### **3.7.1 - Page Top & Tail**
* 1 - Is the quiz name displayed at the top of the page?  
**Desired Result:** Yes  
* 2 - Is the Quiz Link section included?  
**Desired Result:** Yes  
* 3 - Does the Quiz quiz ID in the link match that in the page url?  
**Desired Result:** Yes  

### **3.7.2 - Rounds Collapsible**
* 1 - Is the Rounds section displayed?  
**Desired Result:** Yes  
* 2 - Are the individual Rounds collapsible card expanded by default?  
**Desired Result:** Yes  
* 3 - Does clicking the header collapse the card section beneath if expanded?  
**Desired Result:** Yes  
* 4 - Does clicking the header expand the card section beneath if collapsed?  
**Desired Result:** Yes  
* 5 - Do the number of Rounds heading displayed match the number the User selected when creating the quiz?  
**Desired Result:** Yes  
* 6 - Do the individual categories shown in the heading of each round match those selected when creating the quiz?  
**Desired Result:** Yes 
* 7 - Is the Round Score displayed at the end of the card?  
**Desired Result:** Yes  
* 8 - Prior to the game being started, does the round score state something like "game not started"?  
**Desired Result:** Yes  

### **3.7.3 - Individual Round Collapsible**
* 1 - Does clicking on a round header expand the card beneath if collapsed?  
**Desired Result:** Yes  
* 2 - Does clicking on a round header collapse the card beneath if expanded?  
**Desired Result:** Yes  
* 3 - Does the number of questioned displayed match the number slected by the User when the quiz was created?  
**Desired Result:** Yes  
* 4 - Do the questions match the category listed for the round?  
**Desired Result:** Yes  
* 5 - Is each question listed one beneath the other?  
**Desired Result:** Yes  
* 6 - Is each question numbered sequentially?  
**Desired Result:** Yes  
* 7 - Is the difficulty for each question shown?  
**Desired Result:** Yes  
* 8 - Do the quantity of questions for each difficulty match the choices made when the quiz was created?  
**Desired Result:** Yes  
* 9 - Does clicking on an incorrect answer turn that answer red?  
**Desired Result:** Yes  
* 10 - Does clicking on an incorrect answer turn the correct answer green?  
**Desired Result:** Yes  
* 11 - Does clicking on an incorrect answer have no affect on the other two incorrect answers?  
**Desired Result:** Yes  
* 12 - Does clicking on an incorrect answer add one to the score?  
**Desired Result:** No  
* 13 - Does clicking on the correct answer turn that answer green?  
**Desired Result:** Yes  
* 14 - Does clicking on the correct answer have no affect on the incorrect answers?  
**Desired Result:** Yes  
* 15 - Does clicking on the correct answer add one to the score?  
**Desired Result:** Yes  
* 16 - Does clicking on the correct answer display a modal stating the total score?  
**Desired Result:** Yes  
* 17 - Does clicking the X on the corect score modal close the modal?  
**Desired Result:** Yes  
* 18 - Does clicking on the modal side area close the modal?  
**Desired Result:** Yes  
* 16 - Once a question has been selected, can it or any of the questions in that block be clicked on?  
**Desired Result:** No
* 17 - Does the Round Score reflect the number of questions answered correctly in the round?  

### **3.7.4 - Total Quiz Score Section**
* 1 - Is the Total Quiz Score section displayed beneath the Rounds section?  
**Desired Result:** Yes  
* 2 - Prior to the game being started, does the Total Quiz Score state something like "game not started"?  
**Desired Result:** Yes 
* 3 - Does the Total Quiz Score reflect the total for all questions answered and rounds played?  
**Desired Result:** Yes  