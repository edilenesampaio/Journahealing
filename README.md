# Journahealing

Journahealing is a web app where it's users are welcome to create a profile and write journals about their daily life 
or journals about traveling. The idea of making Journahealing came from a personal reason of having a safe space where the user can write about whatever they are feeling or maybe document some cool trip they've done.


# About me

Edilene is graduated with a Business Administration degree. She moved to the US about five years ago to study English as a Second Language. Prior to joining Hackbright Academy, she worked as an Administrative Assistante for a real estate company in Chicago, where she helped tenants and landlords with various inqueries. Combining her passion for technology and writing, she got inspired to create Journahealing, where its users can write about anything.

# Tech stack

certifi==2023.11.17
click==8.0.1
cloudinary==1.38.0
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
greenlet==3.0.3
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
psycopg2-binary==2.9.3
six==1.16.0
SQLAlchemy==1.4.18
urllib3==2.1.0
Werkzeug==2.0.1

# Features

The app allows users to create an account, log in and log out of their account.

The backend was built in Python and Flask and it was complemented by a user-friendly front-end interface created with HTML, CSS, and JavaScript. 


When a user logs in, they are taken to their profile page, where they can write a new journal or travel journal. The user can also visualize previous written journals.



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

