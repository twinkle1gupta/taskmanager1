# app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 987651234)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:Twinkle2911@localhost/taskdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
