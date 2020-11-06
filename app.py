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
    # Get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    _id = mongo.db.users.find_one("_id")
    email = mongo.db.users.find_one("email")
    quizzes = list(mongo.db.quizzes.find())
    return render_template("profile.html",
        username=username, profile_id=_id, email=email, quizzes=quizzes)


@app.route("/logout")
def logout():
    flash("You're logged out")
    # Remove session cookie
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create", methods=["GET", "POST"])
def create():
    existing_user = mongo.db.users.find_one()

    if request.method == "POST":

        quiz_details = {
            "user_id": existing_user["_id"],
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

        # Checks to see if the User is logged in or not
        if "user" in session:
            flash("Quiz Successfully Created!")
            return render_template("quiz_admin.html")
        else:
            # Session added so as to correctly redirect User once registered
            session["quiz_name"] = request.form.get("quiz_name")
            flash("Please register or login to finish your quiz.")
            return redirect(url_for("register"))

    return render_template("create.html")

@app.route("/quiz_admin")
def quiz_admin():
    return render_template("quiz_admin.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
