import locale
import os

from flask import Flask, Blueprint, session
from flask_ckeditor import CKEditor

from flask_restful import Api

from app.ServerManager import ServerManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)


blueprint = Blueprint('api', __name__, template_folder='templates')
#
# db = SQLAlchemy()
# db.init_app(application)
# migrate = Migrate(application, db, render_as_batch=True)
server_manager = ServerManager()





#from app import models
