from flask import Flask
from .conferencia import CCConferencia
from .blueprints.admin import CCAdmin
CCApp = Flask(__name__)

CCApp.register_blueprint(CCConferencia)
CCApp.register_blueprint(CCAdmin)
