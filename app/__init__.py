#to initialize application and import necessary contents

from flask import Flask
from app.extensions import db , migrate
from app.routes import task_bp , user_bp
from app.config import Config

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(task_bp,url_prefix ='/api')
    app.register_blueprint(user_bp,url_prefix ='/api')

    return app