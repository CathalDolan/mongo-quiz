import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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

        # Check if user email already exists in DB
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")}
        )

        if existing_user:
            flash("Email already exists", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new User into "session" via a session cookie
        session["user"] = request.form.get("username")
        flash("Registration Successful!")
        # Username needs to be from Session so as to match Profile page
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")}
        )

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):

                    # The cookie is called "Session" and contains "user"
                    session["user"] = existing_user["username"]
                    flash("Welcome, {}".format(existing_user["username"]))
                    return redirect(url_for("profile", username=session["user"]))

            else:
                flash("Incorrect password and/or Username")
                return redirect(url_for("login"))

        else:
            flash("Incorrect password and/or Username")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    email = mongo.db.users.find_one("email")
    return render_template("profile.html", username=username, email=email)


@app.route("/logout")
def logout():
    flash("You're logged out")
    # Remove session cookie
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        quiz_details = {
            "quiz_name": request.form.get("quiz_name"),
            "rounds": request.form.get("rounds"),
            "questions": request.form.get("rounds"),
            "category1": request.form.get("category1"),
            "easy": request.form.get("easy"),
            "medium": request.form.get("medium"),
            "hard": request.form.get("hard"),
            "invitees": request.form.get("invitees")
        }
        # Insert the dictionary into the database
        mongo.db.quizzes.insert_one(quiz_details)

        flash("Quiz Successfully Created!")
        return render_template("profile.html")

    return render_template("create.html")


@app.route("/quiz_admin/<quiz_id>")
def quiz_admin(quiz_id):

    quiz_id = mongo.db.quizzes.find_one(
        {"username": session["user"]})["username"]

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("quiz_admin.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
