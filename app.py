import os
import requests
import json
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Check if User email already exists in DB
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")}
        )

        # Activates if the email is already registered
        if existing_user:
            flash("Email already exists", "error")
            return redirect(url_for("register"))

        # "else" Register User and add form data to the database...
        register = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # ...and put the new User into "session" via a session cookie
        session["user"] = request.form.get("username")

        flash("Registration Successful!")
        # Username needs to be from Session so as to match Profile page
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Check to see if the email is already registered
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")}
        )

        # Activates if the email is already registered
        if existing_user:
            # Compares registered password to that entered by the User
            if check_password_hash(
                existing_user["password"], request.form.get("password")):

                    # If password match, a session cookie is added
                    session["user"] = existing_user["username"]

                    # Checks if there is a Quiz session in place
                    if "quiz_name" in session:
                        session.pop("quiz_name")
                        flash("Quiz Creation and Login Successful!")
                        return render_template("quiz_admin.html")
                    else:
                        flash("Welcome, {}".format(existing_user["username"]))
                        # Username needs to be from Session so as to match Profile page
                        return redirect(url_for("profile", username=session["user"]))

            # If password doesn't match
            else:
                flash("Incorrect password and/or Username")
                return redirect(url_for("login"))

        # If User email is not already registered
        else:
            flash("Incorrect password and/or Username")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get the session user's details from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    print(f"USERNAME: {username}")

    quizzes = list(mongo.db.quizzes.find())
    for quiz in quizzes:
        for invitees in quiz["invitees"]:
            print("INVITEES: ", invitees)
    return render_template("profile.html",
        username=username, quizzes=quizzes)


@app.route("/logout")
def logout():
    flash("You're logged out")
    # Remove session cookie
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create", methods=["GET", "POST"])
def create():

    # current date and time
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y")

    if request.method == "POST":

        # Categories API call is done in getCategoriesFn() in script.js
        # Var so Categories go into DB as a list from form
        # Categories converted to JSON Objects
        categories =[]
        num = 1
        while True:
            if 'round{}'.format(num) in request.form:
                print("\n\nCategory: ", request.form.get("round{}".format(num)), "\n\n")
                # categories.append(json.loads(request.form.get("round{}".format(num))))
                categories.append(json.loads(request.form.get("round{}".format(num))))
                num +=1
            else:
                break

        # Var so Difficulties go into DB as a dict in a lis from form
        difficulty = [{
            'easy': int(request.form.get('easy')),
            'medium': int(request.form.get('medium')),
            'hard': int(request.form.get('hard'))
            }]

        existing_user = mongo.db.users.find_one(
        {"username": session["user"]})

        # Var so Invitees go into DB as a list from form
        invitee_list = request.form.get("invitees")
        invitees = invitee_list.replace(',', ' ').split()
        invitees.append(existing_user["email"])

        # Capture of all quiz details from form
        quiz_details = {
            "user_id": existing_user["_id"],
            "quiz_master": existing_user["username"],
            "quiz_name": request.form.get("quiz_name"),
            "rounds": int(request.form.get("rounds")),
            "questions": int(request.form.get("questions")),
            "categories": categories,
            "difficulty": difficulty,
            "type": "multiple",
            "easy": int(request.form.get("easy")),
            "medium": int(request.form.get("medium")),
            "hard": int(request.form.get("hard")),
            "invitees": invitees,
            "created": timestampStr
        }
        # Insert the quiz_details dictionary into the database
        # Creating a var allows the data to be returned. Needed so as to get _id
        result = mongo.db.quizzes.insert_one(quiz_details)

        # Get the total of the three Difficulty fields...
        difficulty_total = quiz_details['easy'] + quiz_details['medium'] + quiz_details['hard']
        # ...then validate whether Difficulty totals match the number of Questions
        if difficulty_total == quiz_details['questions']:
            flash("Your quiz has been created!")
            return redirect(url_for("quiz_admin", quiz_id=result.inserted_id))
        else:
            flash("The total for all 3 Difficulty levels must equal the number of questions.")
            return render_template("create.html", quiz_details=quiz_details)

    # quiz_details being empty is to do with redirection after register/login if Quiz create beforehand
    return render_template("create.html", quiz_details="")


@app.route("/update_quiz/<quiz_id>", methods=["GET", "POST"])
def update_quiz(quiz_id):

    existing_user = mongo.db.users.find_one(
        {"username": session["user"]})

    # current date and time
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y")

    if request.method == "POST":

        categories =[]
        num = 1
        while True:
            if 'round{}'.format(num) in request.form:
                categories.append(json.loads(request.form.get("round{}".format(num))))
                num +=1
            else:
                break

        difficulty = [{
            'easy': int(request.form.get('easy')),
            'medium': int(request.form.get('medium')),
            'hard': int(request.form.get('hard'))
            }]

        invitee_list = request.form.get("invitees")
        invitees = invitee_list.replace(',', ' ').split()

        quiz_details = {
            "user_id": existing_user["_id"],
            "quiz_master": existing_user["username"],
            "quiz_name": request.form.get("quiz_name"),
            "rounds": int(request.form.get("rounds")),
            "questions": int(request.form.get("questions")),
            "categories": categories,
            "difficulty": difficulty,
            "type": "multiple",
            "easy": int(request.form.get("easy")),
            "medium": int(request.form.get("medium")),
            "hard": int(request.form.get("hard")),
            "invitees": invitees,
            "created": timestampStr
        }

        # Validate whether Difficulty totals match the number of Questions
        difficulty_total = quiz_details['easy'] + quiz_details['medium'] + quiz_details['hard']
        if difficulty_total == quiz_details['questions']:
            mongo.db.quizzes.update({"_id":ObjectId(quiz_id)}, quiz_details)
            flash("Quiz details updated")
            return redirect(url_for("quiz_admin", quiz_id=quiz_id))
        else:
            flash("The total for all 3 Difficulty levels must equal the number of questions.")
            return render_template("quiz_admin.html")

    return render_template("quiz_admin.html")


@app.route("/quiz_admin/<quiz_id>")
def quiz_admin(quiz_id):

    # Username data required fpor passing into the page
    username = mongo.db.users.find_one(
        {"username": session["user"]})

    # Extracts the quiz _id from the URL
    # Allows the Quiz displayed to match the one opened from the Profile
    url = str(request.base_url)
    url_quiz_id = url.split('/')[-1]

    # Extracts quiz details from DB
    quiz = mongo.db.quizzes.find_one({"_id": ObjectId(url_quiz_id)})

    # Extract the token from the API
    url = "https://opentdb.com/api_token.php?command=request"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    quiz_token = json.loads(response.text.encode("utf8"))["token"]

    quiz_questions = []

    # Extracts the Categories from the DB
    # Enumerate produces a loop count/index
    for category in quiz['categories']:
        category_id = str(category['id'])

        for difficulty in quiz['difficulty']:

            # Extract the Easy Questions from the API
            if int(difficulty['easy']) > 0:
                easy_amount = str(difficulty['easy'])
                url = "https://opentdb.com/api.php?amount=" + easy_amount + "&category=" + category_id + "&difficulty=easy&type=multiple&token=" + quiz_token
                payload = {}
                headers = {}
                q_response1 = requests.request("GET", url, headers=headers, data=payload)
                easy_questions = json.loads(q_response1.text.encode("utf8"))["results"]
                quiz_questions.append(easy_questions)

                for all_details in easy_questions:
                    all_details['all_answers'] = all_details['incorrect_answers']
                    all_details['all_answers'].append(all_details['correct_answer'])
                    random.shuffle(all_details['all_answers'])

            # Extract the Medium Questions from the API
            if int(difficulty['medium']) > 0:
                medium_amount = str(difficulty['medium'])
                url = "https://opentdb.com/api.php?amount=" + medium_amount + "&category=" + category_id + "&difficulty=medium&type=multiple&token=" + quiz_token
                payload = {}
                headers = {}
                q_response2 = requests.request("GET", url, headers=headers, data=payload)
                medium_questions = json.loads(q_response2.text.encode("utf8"))["results"]
                quiz_questions.append(medium_questions)

                for all_details in medium_questions:
                    all_details['all_answers'] = all_details['incorrect_answers']
                    all_details['all_answers'].append(all_details['correct_answer'])
                    # Shuffle documentation from https://note.nkmk.me/en/python-random-shuffle/
                    random.shuffle(all_details['all_answers'])

            # Extract the Hard Questions from the API
            if int(difficulty['hard']) > 0:
                hard_amount = str(difficulty['hard'])
                url = "https://opentdb.com/api.php?amount=" + hard_amount + "&category=" + category_id + "&difficulty=hard&type=multiple&token=" + quiz_token
                payload = {}
                headers = {}
                q_response3 = requests.request("GET", url, headers=headers, data=payload)
                hard_questions = json.loads(q_response3.text.encode("utf8"))["results"]
                quiz_questions.append(hard_questions)

                for all_details in hard_questions:
                    all_details['all_answers'] = all_details['incorrect_answers']
                    all_details['all_answers'].append(all_details['correct_answer'])
                    random.shuffle(all_details['all_answers'])

    return render_template("quiz_admin.html", quizzes=[quiz], quiz_questions=quiz_questions, url_quiz_id=url_quiz_id, username=username)


@app.route("/remove_quiz/<quiz_id>")
def remove_quiz(quiz_id):

    username = mongo.db.users.find_one(
        {"username": session["user"]})
    quiz = mongo.db.quizzes.find_one({"_id": ObjectId(quiz_id)})

    # Advanced MongoDb provided by tutor support with reference to:
    # https://docs.mongodb.com/manual/reference/operator/update/pull/
    mongo.db.quizzes.update(
        {"_id": ObjectId(quiz_id)},
        {"$pull": { "invitees": str(username['email'])}}
    )
    flash("Quiz successfully removed")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_quiz/<quiz_id>")
def delete_quiz(quiz_id):

    username = mongo.db.users.find_one(
        {"username": session["user"]})

    mongo.db.quizzes.remove({"_id": ObjectId(quiz_id)})
    flash("Quiz successfully deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
