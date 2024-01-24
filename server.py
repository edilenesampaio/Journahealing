"""Server for journahealing app."""

from flask import (Flask, jsonify, render_template, request, flash, session, redirect, url_for)
import cloudinary.uploader
import os
from datetime import datetime



CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dpgsshgwg"

from model import connect_to_db, db, User, Journal, Travel_Journal, Photo
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """"View homepage."""

    return render_template('homepage.html')


@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users= users)



@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')
 
    user = crud.get_user_by_email(email)
    if user:
        flash("Can't create an account with this email. Please, try again!")

    else: 
        user = crud.create_user(user_name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please, log in.")

    return redirect("/")

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/login", methods=["POST"])
def user_login():

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if not user:
        flash("Wrong login")

    elif password != user.password:
        flash("Incorrect password")

    else: 
        session['current_user'] = user.email
        flash("Logged in!")
        return redirect("/profile")
    
    return redirect("/")


# @app.route("/logout", methods=['POST'])
# def user_logout():
#     """Log user out of the session."""
    
#     if session.get('current_user'):
#         del session['current_user']
#     flash('Logged out!')
#     return redirect("/")




@app.route("/profile")
def show_profile():
    """Show profile page."""

    if 'current_user' not in session:
        flash("Please log in")
        return redirect("/")
    
    else:
        user = crud.get_user_by_email(session["current_user"])

        journals = Journal.query.filter_by(creator=user.user_id).all()
        travel_journals = Travel_Journal.query.filter_by(creator=user.user_id).all()
       

        if journals is None:
            journals = []

        if travel_journals is None:
            travel_journals = []

        # all_journals = journals + travel_journals
        # print(all_journals)
        

    return render_template("profile.html", user=user, journals=journals, travel_journals=travel_journals)



@app.route("/save_journal", methods=['POST'])
def create_new_journal():
    """Create a new journal."""

    content = request.json.get('content')
    user = crud.get_user_by_email(session["current_user"])
    created_at = datetime.now()
    journal = crud.create_new_journal(content, created_at, user)
    db.session.add(journal)
    db.session.commit()
    print(journal)
    return jsonify({'content': content})    


#get information from get form
#create crud function , create_new_journal
#maybe flash a message "new journal"
#make page refresh, redirect to profile

    # request.form.get



@app.route("/save_travel_journal", methods=['POST'])
def create_new_travel_journal():
    """Create a new journal."""

    content = request.json.get('content')
    user = crud.get_user_by_email(session["current_user"])
    created_at = datetime.now()
    travel_journal = crud.create_new_travel_journal(content, created_at, user, address)
    db.session.add(travel_journal)
    db.session.commit()
    print(travel_journal)
    return jsonify({'content': content})    


# if the user update pictures to their travel_journal
    # my_file = request.files['my-file']
    # if my_file: 
    #     img_url = upload_to_cloudinary(my_file)
    #     image = crud.create_image(travel_journal.travel_journal_id, img_url)

    # db.session.add(image)
    # db.session.commit()


# @app.route("/photo", methods=['POST'])
# def add_photo():

#     my_file = request.files['my-file']

#     result = cloudinary.uploader.upload(my_file,
#                                         api_key=CLOUDINARY_KEY,
#                                         api_secret=CLOUDINARY_SECRET,
#                                         cloud_name=CLOUD_NAME)
                                 
#     img_url = result['secure_url']



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)