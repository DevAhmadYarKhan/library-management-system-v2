import os

class Config:
    # Flask and some of its extensions uses the value of 'SECRET_KEY' as a cryptographic key,
    # useful to generate signatures and tokens. For example, the Flask-WTF extension uses
    # it to protect webforms against CSRF attacks. The following line of code looks for
    # an environment variable also named 'SECRET_KEY', else it uses the hardcoded string
    # to set the value of the variable.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'