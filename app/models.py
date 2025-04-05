#models with SQLAlchemy

from datetime import datetime
from app.extensions import db

class TaskManager(db.Model):
    id=db.column(db.Integer,primary_key=True)
    task_name=db.column(db.String(100),nullable=False)
    description=db.column(db.String(100),nullable=True)
    status=db.column(db.Boolean,default=True)
    priority=db.column(db.String(100),nullable=True)
    assigned_user=db.column(db.String(100),nullable=False)
    created_at=db.column(db.DateTime,default=datetime.utcnow)
    updated_at=db.column(db.DateTime,default=datetime.utcnow)

class TaskLogger(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    task_manager_id=db.Column(db.Integer,db.ForeignKey('task_manager.id'),nullable=False)
    log_date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)