import os


# Grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

# Defines the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)