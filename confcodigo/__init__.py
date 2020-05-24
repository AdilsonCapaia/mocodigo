from flask import Flask,render_template
from . import conferencia
from .blueprints.admin import CCAdmin
CCApp = Flask(__name__)

CCApp.register_blueprint(conferencia.CCConferencia)
CCApp.register_blueprint(CCAdmin)

@CCApp.route('/')
def inicio():
    return render_template('inicio.html')
