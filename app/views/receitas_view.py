from flask import Blueprint
from app.services.receitas.receitas_manage_csv import listar_receitas
from app.services.receitas.receitas_manage_csv import buscar_receitas

bp = Blueprint('receitas_route', __name__)


@bp.route('/receitas')
def lista_receitas():
    return {
        'data': listar_receitas()
    }


@bp.route('/receitas/<nome>')
def busca_receita(nome):
    return {
        'data': buscar_receitas(nome)
    }
