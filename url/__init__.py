#!venv/bin/python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import logging

# Creates global Flask app object
# Sets configuration variables from config.py
app = Flask(__name__)
app.config.from_pyfile('../config.py')

# Creates global SQLAlchemy and Migrate objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Creates global Manager object and allows migrate.py to work
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from url import views, models
