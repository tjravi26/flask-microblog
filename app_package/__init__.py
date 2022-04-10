from flask import Flask

# Created a Config class in /config.py and imported it.
from config import Config

app = Flask(__name__)

# Config class which contains flask configurations.
app.config.from_object(Config)

from app_package import routes  # noqa: E402, F401
