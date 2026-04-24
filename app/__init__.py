from flask import Flask # Import the Flask class from the flask package.

app = Flask(__name__) # Initialise app as an object of type Flask.

from app import routes # Imported at bottom to avoid circular import.