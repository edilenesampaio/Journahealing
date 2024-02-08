# Journahealing

Journahealing is a web app where it's users are welcome to create a profile and write journals about their daily life 
or about traveling. The idea of making Journahealing came from a personal reason of having a safe space where the user can write about whatever they are feeling or maybe document some cool trip they've done.


# About me

Edilene is graduated with a Business Administration degree. She's originally from Brazil, and moved to the US about six years ago to study and learn English. Prior to joining Hackbright Academy, she worked as an Administrative Assistante for a real estate company in Chicago, where she helped tenants and landlords navigate their relationship. Combining her passion for technology and writing, she got inspired to create Journahealing, a digital version of a journaling space, where its users can write about anything.

# Tech stack

* Python
* Flask
* HTML
* JavaScript
* Jinja2
* PostgreSQL
* SQLAlchemy
* CSS
* Bootstrap
* Cloudinary API

# Features

The app allows users to create an account, log in and log out of their account.

The backend was built with Python and Flask and it was complemented by a user-friendly front-end interface created with HTML, CSS, and JavaScript. 


When a user logs in, they are taken to their profile page, where they can input their journal or travel journal
entries. A user can create a journal by simply writing inside the content box, and once done, click in the "save" button.
The same writing process is used for travel journals, with the extra option to add pictures and an address for your entry. 
I used the cloudinary API to allow users to upload a picture to their travel journals. Both features used AJAX to create an interactive environment, allowing users to save their journals without a page refresh.

Under the section My Journals, users are able to visualize the journals and travel journals previously saved, displaying its written content and data time.

All the data entered is stored in my Postgres database using SQLAlchemy. The application allows the user to interact with the database, being able to add, edit and delete journal and travel journal entries.

I styled my app utilizing a combination of CSS and Bootstrap creating a well-organized layout.

This application was created from a personal perspective where the user would have a safe space to digitally write about their feelings, life or anything they would like to, as well writing about their traveling experiences and adventures. 

# Installing Journahealing
Clone this repo into your computers directory:
```python
https://github.com/edilenesampaio/Journahealing.git
```

Create your virtual environment inside your Journahealing Directory:
```python
virtualenv env
```

Activate the environment:
```python
source env/bin/activate
```

Install the Requirements:
```python
pip install -r requirements.txt
```

Create your database(db):
```python
createdb journals
  python3 -i model.py
       >>db.create_all()
```

Sign up to use the [Cloudinary API](https://cloudinary.com)

Save your API Key in a file named secrets.sh in the following format:
```python
CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUDINARY_NAME = ""
```

Run the application:
```python
python3 server.py
```

You can now access Journahealing at 'localhost:5000/' and start writing your journals!

