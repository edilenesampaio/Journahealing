"""Server for journahealing app."""

from flask import (Flask, render_template, request, flash, session, redirect, url_for)
import cloudinary.uploader
import os



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


# @app.route("/users")
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template("all_users.html", users= users)



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




# @app.route("/profile")
# def show_profile():
# """Show user profile."""



#     if 'current_user' not in session:
#         flash("Please, log in")
#         return redirect("/")
    
#     else:
#         user = crud.get_user_by_email(session["current_user"])
        
#         # Journals = Journals.query.filter_by(creator=user.user_id).all()

#         if journal is None:
#             journal = []
    
#         #for user_journals in user_journals:

#         return render_template("profile.html", user=user, journal=journal)

@app.route("/profile")
def show_profile():
    """Show profile page."""

    if 'current_user' not in session:
        flash("Please log in")
        return redirect("/")
    
    else:
        user = crud.get_user_by_email(session["current_user"])

        journals = Journal.query.filter_by(creator=user.user_id).all()

        # if journals in None:
        #     journals = []

        # for journal in journals:

        return render_template("profile.html", user=user, journals=journals)





@app.route("/journal", methods=['POST'])
def show_journal():
    """Show user journals."""

    journal = request.json.get('new_journal')
    user = crud.get_user_by_email(session["current_user"])
    user.journal = int(journal)
    db.session.commit()
    print(user.journal)
    return jsonify({'journal': journal})    



# @app.route("travel_journal", methods=['POST'])
# def all_travel_journals():
#     """"View all user travel journals.”””


#     travel_journal = crud.get_travel_journals()

#     return render_template("all_travel_journals.html", travel_journal=travel_journal)


# @app.route("/save_travel_journal", methods=['POST'])
# def save_travel_journal():
#     """Save user travel journals to profile"""

#     creator = crud.get_user_by_email(session["current_user"]).user_id

#     save_content = request.json.get('save_content')
#     save_address = request.json.get('save_address')
#     travel_journal_to_save = request.json.get('travel_journal_to_save')
#     saved_travel_journal = crud.create_travel_journal(creator, content, address)
#     original_travel_journal = crud.get_user_travel_journal_by_id(travel_journal_to_save)
#     db.session.add(saved_travel_journal)
#     db.session.commit()
#     print(saved_travel_journal)


# @app.route("/photo", methods=['POST'])
# def add_photo():

#     my_file = request.files['my-file']

#     result = cloudinary.uploader.upload(my_file,
#                                         api_key=CLOUDINARY_KEY,
#                                         api_secret=CLOUDINARY_SECRET,
#                                         cloud_name=CLOUD_NAME)
                                 
#     img_url = result['secure_url']



# @app.route("/logout", methods=['POST'])
# def user_logout():
#     """Log user out of the session."""
    
#     if session.get('current_user'):
#         del session['current_user']
#     flash('Logged out!')
#     return redirect("/")



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)