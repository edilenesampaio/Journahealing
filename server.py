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


@app.route("/logout", methods=['POST'])
def user_logout():
    """Log user out of the session."""
    
    if session.get('current_user'):
        del session['current_user']
    flash('Logged out!')
    return redirect("/")




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
    return jsonify({'content': content, 'journal_id': journal.journal_id, 'created_at': created_at})    


@app.route("/journal/<journal_id>")
def show_journals(journal_id):
    """View all user journals."""


    journal = crud.get_journal_by_id(journal_id)

    return render_template("journals_details.html", journal=journal)



@app.route("/delete_journal", methods=['POST'])
def delete_journal():
        """Delete a journal."""

        delete_journal = request.form.get('journal_id')
        print(delete_journal)
        print(type(delete_journal))
        del_journal = crud.get_journal_by_id(delete_journal)
        db.session.delete(del_journal)
        db.session.commit()
        return redirect('/profile')



@app.route("/edit_journal", methods=['POST'])
def edit_journal():
        """Edit a journal."""

        edit_journal = request.form.get('journal_id')
        edit_content = request.form.get('journal_content')
        print(edit_journal)
        print(type(edit_journal))
        print(edit_content)
        print(type(edit_content))
        edi_journal = crud.get_journal_by_id(edit_journal)
        print(edi_journal)
        edi_journal.content = edit_content
        db.session.commit()
        return redirect('/profile')



@app.route("/save_travel_journal", methods=['POST'])
def create_new_travel_journal():
    """Create a new travel journal."""

    content = request.form.get('content')
    address = request.form.get('address')
    user = crud.get_user_by_email(session["current_user"])
    created_at = datetime.now()
    travel_journal = crud.create_travel_journal(content, created_at, address, user)
    db.session.add(travel_journal)
    db.session.commit()
    print(travel_journal)

    image = request.files.get('image')
    if image: 
        result = cloudinary.uploader.upload(image,
                                             api_key=CLOUDINARY_KEY,
                                            api_secret=CLOUDINARY_SECRET,
                                            cloud_name=CLOUD_NAME)
        img_url = result['secure_url']
        print(img_url)
        image = crud.create_image(travel_journal.travel_journal_id, img_url, created_at, user)

        db.session.add(image)
        db.session.commit()


    return jsonify({'travel_journal_id': travel_journal.travel_journal_id, 'content': content, 'created_at': created_at, 'address': address})    


@app.route("/travel_journal/<travel_journal_id>")
def show_travel_journals(travel_journal_id):
    """View all user travel journals."""


    travel_journal = crud.get_travel_journal_by_id(travel_journal_id)

    return render_template("travel_journals_details.html", travel_journal=travel_journal)

# if the user update pictures to their travel_journal
    

@app.route("/delete_travel_journal", methods=['POST'])
def delete_travel_journal():

        delete_travel_journal = request.form.get('travel_journal_id')
        print(delete_travel_journal)
        print(type(delete_travel_journal))
        del_travel_journal = crud.get_travel_journal_by_id(delete_travel_journal)
        db.session.delete(del_travel_journal)
        db.session.commit()
        return redirect('/profile')



@app.route("/edit_travel_journal", methods=['POST'])
def edit_travel_journal():
        """Edit a travel journal."""

        edit_travel_journal = request.form.get('travel_journal_id')
        edit_content = request.form.get('travel_journal_content')
        print(edit_travel_journal)
        print(type(edit_travel_journal))
        print(edit_content)
        print(type(edit_content))
        edi_travel_journal = crud.get_travel_journal_by_id(edit_travel_journal)
        print(edi_travel_journal)
        edi_travel_journal.content = edit_content
        db.session.commit()
        return redirect('/profile')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)