"""Models for journahealing app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """An user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    
    journals = db.relationship("Journal", back_populates="user")
    
    def __repr__(self):
        """Show info about the user."""
        
        return f"<User user_id={self.user_id} email={self.email}>"


class Journal(db.Model):
    """A regular journal."""

    __tablename__ = "journals"

    journal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.Text, default="Content")
    date_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    
    user = db.relationship("User", back_populates="journals")

    def __repr__(self):
        return f"<Journal journal_id={self.journal_id} content={self.content}>"
    
class Travel_Journal(db.Model):
    """A travel journal."""

    __tablename__ = "travel_journals"

    travel_journal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.Text, default="Content")
    date_time = db.Column(db.DateTime) 
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    address = db.Column(db.String)

    
    user = db.relationship("User", back_populates="travel_journals")

    def __repr__(self):
        return f"<Travel_journal travel_journal_id={self.travel_journal_id} content={self.content}>"


class Photo(db.Model):
    """Posted photos."""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    date_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    image = db.Column(db.String)

    photo = db.relationship("Photos", back_populates="travel_journals")
    user = db.relationship("User", back_populates="travel_journals")

    def __repr__(self):
        return f"<Photos photos_id={self.photos_id} image={self.image}>"



def connect_to_db(flask_app, db_uri="postgresql:///journals", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
