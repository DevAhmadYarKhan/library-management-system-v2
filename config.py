import os

# Basedir is an absolute path to the folder this file is in
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask and some of its extensions uses the value of 'SECRET_KEY' as a cryptographic key,
    # useful to generate signatures and tokens. For example, the Flask-WTF extension uses
    # it to protect webforms against CSRF attacks. The following line of code looks for
    # an environment variable also named 'SECRET_KEY', else it uses the hardcoded string
    # to set the value of the variable.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Again, if environment variable named 'DATABASE_URL' is not set, then the url to an
    # app.db file in the folder this file is in is provided.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')