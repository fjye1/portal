import datetime
from datetime import datetime, timezone, timedelta
from flask_login import UserMixin
from app.extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    
    # This links the User to their Projects
    # 'backref' adds a .owner property to the Project model
    projects = db.relationship('Project', backref='owner', lazy=True)
    

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # The Foreign Key links the project to a specific User ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
class ProjectAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)  # e.g. 'kit_website'
    email = db.Column(db.String(200), nullable=False)