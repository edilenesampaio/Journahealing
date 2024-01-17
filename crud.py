"""CRUD operations."""

from model import db, User, Journal, Travel_Journal, Photo, connect_to_db

def create_user(user_name, email, password):
    """Create and return a new user."""

    user = User(
        user_name=user_name,
        email=email,
        password=password,
    )

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by id."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""
    
    return User.query.filter(User.email == email).first()


def create_journal(content, creator, date_time):
    """Create and return a new journal"""

    journal = Journal(
        content=content,
        creator=creator,
        date_time=date_time,
    )
    
    return journal

def get_journal(user):

    return Journal.query.filter(Journal.user == user).first()

def get_journals():
 
    return Journal.query.all()


def get_journal_by_id(journal_id):
    

    return Journal.query.get(journal_id)


# def create_travel_journal(content, data_time, address):

#     travel_journal = Travel_Journal(
#         content=content, 
#         data_time=data_time, 
#         address=address,
#     )

#     return travel_journal

# def get_travel_journal(user):
#     """Get travel journal"""


# def add_photo(date_time, image):
#       """Add photos to a travel journal."""
    
#     photo = Photo( 
#         date_time=date_time,
#         image=image,
#     )
    
#     return photo







if __name__ == '__main__':
    from server import app
    connect_to_db(app)