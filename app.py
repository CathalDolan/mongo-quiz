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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Check if Username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # If there is an existing user with that name...
        if existing_user:
            
            return redirect(url_for("register"))

        # This acts as the "else" statement if no matching Username is found
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Insert the dictionary into the database
        mongo.db.users.insert_one(register)

        # Put the new User into "session" via a session cookie
        session["user"] = request.form.get("username").lower()
        print(f"User in the session is this: {session['user']}, user form the request is this: {request.form.get('username')}!!!")
        flash("Registration Successful!")
        # Username needs to be from Session so as to match Profile page
        return redirect(url_for("home", username=session["user"]))
        print(session)

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Check if Username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # If username does exist then...
        if existing_user:
            # Compare passwords using Werkzeug hash to check for a match
            # If it does add a session cookie and flash message
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):

                        # The cookie is called "Session" and contains "user"
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        # Redirects User to Profile page, just like Register
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # If the password doesn't match then...
                flash("Incorrect password and/or Username")
                return redirect(url_for("login"))

        else:
            # If Username doesn't exist then...
            flash("Incorrect password and/or Username")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
