import os

from flask import Flask, session, render_template, request, redirect, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from helpers import apology, login_required

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("building.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user In """

    # Forgot any user_id
    session.clear()

    # User reached the route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username is submitted
        if not request.form.get("username"):
            return apology("Username is not submitted", 403)

        # Ensure password is submitted
        if not request.form.get("password"):
            return apology("password is not submitted", 403)

        # Hash the password
            # TODO

        # Query database with name and hashed password
            # TODO

        # Add user to session and redirect to homepage if success else error out
            # TODO

        return render_template("building.html")

    # User reached via GET (as by clicking on a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register new User """

    # Forgot any user_id
    session.clear()

    # User reached to route via POST (as by submitting a form as POST)
    if request.method == "POST":

        # Ensure username is submitted
        if not request.form.get("username"):
            return apology("Username is not submitted", 403)

        # Ensure password is submitted
        if not request.form.get("password"):
            return apology("Password is not submitted", 403)

        # Ensure confirm password and password are same
        if not request.form.get("conf_password") == request.form.get("password"):
            return apology("Password doesn't match", 403)

        # Hash the password

        # Check if username is not already existed in db, if exists error out

        # Add a new entry to db

        # store user_id in session

        return render_template("building.html")

    # User reached the route via GET (as by clicking on a link or redirect)
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    """ Log user out """

    # Forgot user_id
    session.clear()

    # Redirect to homepage
    return redirect("/")

@app.route("/search")
def search():
    """ Searches for book which matches the query """

    # Ensure parameter is present
    if not request.args.get("q"):
        raise RuntimeError("missing search string")

    # Query db with the string LIMIT result to 10
        # TODO

    # send back as json
        # TODO

    return jsonify({})

