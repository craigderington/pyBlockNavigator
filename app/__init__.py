# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def load_models():
    from app.models import User, Role

load_models()


def init_extension(app):
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)


def init_views(app):
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)


def create_app(config=config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extension(app)
    init_views(app)

    return app





