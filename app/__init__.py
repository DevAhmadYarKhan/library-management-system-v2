from config import Config   # Import the Config class from the config module
from flask import Flask # Import the Flask class from the flask package.
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # Initialise app as an object of type Flask.
app.config.from_object(Config)  # Apply the configurations defined by Config class
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # Imported at bottom to avoid circular import.