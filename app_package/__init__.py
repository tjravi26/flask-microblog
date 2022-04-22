import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Created a Config class in /config.py and imported it.
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler  # To send error reports by mail.
from logging.handlers import RotatingFileHandler  # To save a log of errors.


app = Flask(__name__)

# Used to remember user login session.
login = LoginManager(app)

# Forces users to login. Requires the 'login' view function as input.
login.login_view = 'login'

# Config class which contains flask configurations.
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if not app.debug:  # To send error reports by mail.
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app_package import routes, models, errors  # noqa: E402, F401
