from flask import Flask
from . import conferencia
from .blueprints.admin import CCAdmin
CCApp = Flask(__name__)

CCApp.register_blueprint(conferencia.CCConferencia)
CCApp.register_blueprint(CCAdmin)
