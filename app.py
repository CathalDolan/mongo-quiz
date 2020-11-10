import os
import requests
import json
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
@app.route("/home")
def home():
    return render_template("home.html")


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

        # Checks if there is a Quiz session in place
        if "quiz_name" in session:
            session.pop("quiz_name")
            flash("Quiz Creation and Registration Successful!")
            return render_template("quiz_admin.html")
        else:
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
    existing_user = mongo.db.users.find_one(
        {"username": session["user"]})

    # current date and time
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y")

    # Extracting the token from the DB
    url = "https://opentdb.com/api_token.php?command=request"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    quiz_token = json.loads(response.text.encode("utf8"))["token"]

    # Extracting the catagories from the DB
    url = "https://opentdb.com/api_category.php"
    payload = {}
    headers = {}
    cat_response = requests.request("GET", url, headers=headers, data=payload)
    categories = json.loads(cat_response.text.encode("utf8"))["trivia_categories"]
    print("Categories", categories)

    if request.method == "POST":

        quiz_details = {
            "token": quiz_token,
            "user_id": existing_user["_id"],
            "quiz_name": request.form.get("quiz_name"),
            "rounds": int(request.form.get("rounds")),
            "questions": int(request.form.get("questions")),
            "category1": request.form.get("art"),
            "type": "multiple",
            "easy": int(request.form.get("easy")),
            "medium": int(request.form.get("medium")),
            "hard": int(request.form.get("hard")),
            "invitees": request.form.get("invitees"),
            "created": timestampStr
        }
        # Insert the dictionary into the database
        mongo.db.quizzes.insert_one(quiz_details)

        difficulty_total = quiz_details['easy'] + quiz_details['medium'] + quiz_details['hard']

        # Validate whether Difficulty totals match the number of Questions
        if difficulty_total == quiz_details['questions']:
            # Checks to see if the User is logged in or not
            if "user" in session:
                quiz_questions = getRequest(quiz_details)
                print("token", quiz_details['token'])
                flash(quiz_questions)
                return render_template("quiz_admin.html", categories=categories)
            else:
                # Session added so as to correctly redirect User once registered
                session["quiz_name"] = request.form.get("quiz_name")
                flash("Please register or login to finish your quiz.")
                return redirect(url_for("register"))
        else:
            flash("The total for all 3 Difficulty levels must equal the number of questions.")

    return render_template("create.html")


def getRequest(quiz_details):
    print("token 2", quiz_details["token"])
    print("user ID", quiz_details["user_id"])


@app.route("/quiz_admin/<quiz_id>")
def quiz_admin(quiz_id):

    # Extracts the quiz _id from the URL
    url = str(request.base_url)
    print(url)
    url_quiz_id = url.split('/')[-1]
    print(url_quiz_id)
    print(quiz_id)

    quizzes = list(mongo.db.quizzes.find())

    return render_template("quiz_admin.html",
        quizzes=quizzes, url_quiz_id=url_quiz_id)


@app.route("/publish/<quiz_id>", methods=["GET", "POST"])
def publish(quiz_id):

    # current date and time
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y")

    if request.method == "POST":

        published_date = {
            "played": timestampStr
        }
        # Insert the dictionary into the database
        mongo.db.quizzes.insert_one(published_date)

        return render_template("quiz_admin.html")


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
