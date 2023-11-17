
from flask import Flask, Blueprint


from app.ServerManager import ServerManager


app = Flask(__name__)


#blueprint = Blueprint('api', __name__, template_folder='templates')
#
# db = SQLAlchemy()
# db.init_app(application)
# migrate = Migrate(application, db, render_as_batch=True)
server_manager = ServerManager()





#from app import models
