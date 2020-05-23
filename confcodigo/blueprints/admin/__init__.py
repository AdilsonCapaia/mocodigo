from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
CCAdmin = Blueprint('admin',__name__,template_folder='templates'
        ,static_folder='static'  , url_prefix='/admin')

@CCAdmin.route('/')
def CCmostrar():
    pagina='inicio'
    try:
        return render_template('admin/inicio.html',mensagem= CCAdmin.root_path)
    except TemplateNotFound:
        abort(404)

@CCAdmin.route('/admin/')
def CCnaoImplementado():
    raise abort(404)

@CCAdmin.errorhandler(404)
def CCerro(erro):
    return render_template('erro.html')