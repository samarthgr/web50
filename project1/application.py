import os

from flask import Flask, session, render_template, request, redirect, jsonify, url_for
from flask_session import Session

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["CACHE_TYPE"] = "null"


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
        elif not request.form.get("password"):
            return apology("Password is not submitted", 403)

        # Ensure confirm password and password are same
        elif not request.form.get("conf_password") == request.form.get("password"):
            return apology("Password doesn't match", 403)

        # Hashing password before saving to DB (For password protection)
        hash_password = generate_password_hash(request.form.get("password"))
        user_name = request.form.get("username")

        # Insert new user into DB
        try:
            result = db.execute("INSERT INTO users (name, hash) VALUES (:user, :hash) RETURNING id, name",
                            {'user' : user_name, 'hash' :  hash_password})
        except:
            db.rollback()
            return apology("User already registered", 403)
        else:
            db.commit()

        values = []
        for value in result:
            values.append(value)

        # print(values[0][1])
        # print(values[0])

        # Remember which user has registered in
        session["user_id"] = values[0][0]

        # Redirect user to home page
        return redirect("/")

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


@app.route("/books")
def book():
    """ List of books """

    # Query db for 10 books [For now].
    # We can change it to Most popular, recent or most commented
        # TODO

    # Collect the required info and pass it to html

    return render_template("building.html")


@app.route("/book/<int:isbn_number>")
def details(isbn_number):
    """ Details of book """

    # Query the book details from db
        # Check if book exists, if not error out

        # if exists, get details
            # TODO

    # Pass it to frontend

    return render_template("building.html")


@app.route("/review", methods=["POST"])
def review():
    """ Store submitted review of book """

    # Ensure isbn_number is submitted
    if not request.form.get("isbn_number"):
        return apology("Invalid book", 403)

    # Ensure review is submitted
    if not request.form.get("review"):
        return apology("Text is not submitted", 403)

    # Check if book exist, if not error out

    # add review to db

    return redirect(url_for(details, isbn_number=request.form.get("isbn_number")))
