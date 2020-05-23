from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
CCConferencia = Blueprint('conferencia',__name__,template_folder='templates'
                            , url_prefix='/conf')

@CCConferencia.route('/',defaults = {'pagina':'inicio'})
@CCConferencia.route('/<pagina>')
def CCmostrar(pagina):
    try:
        return render_template('%s.html'%pagina,mensagem='Conf Codigo CC')
    except TemplateNotFound:
        abort(404)

@CCConferencia.route('/')
def CCola():
    return "Benvindo"