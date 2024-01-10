"""CRUD operations."""

from model import db, User, Journal, Travel_Journal, Photo, connect_to_db

def create_user(user_name, email, password):
    """Create and return a new user."""




if __name__ == '__main__':
    from server import app
    connect_to_db(app)