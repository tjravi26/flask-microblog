from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Created a Config class in /config.py and imported it.
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)

# Config class which contains flask configurations.
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app_package import routes, models  # noqa: E402, F401
