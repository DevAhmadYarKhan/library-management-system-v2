from config import Config   # Import the Config class from the config module
from flask import Flask # Import the Flask class from the flask package.

app = Flask(__name__) # Initialise app as an object of type Flask.
app.config.from_object(Config)  # Apply the configurations defined by Config class

from app import routes # Imported at bottom to avoid circular import.