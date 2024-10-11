from flask_appbuilder import ModelView, AppBuilder
from flask_appbuilder.models.sqla.interface import SQLAInterface
from models import Aluno, Informacoes
from run import db, appbuilder


class AlunoModelView(ModelView):
    datamodel = SQLAInterface(Aluno)
    related_views = []  # Corrigido para o ModelView correspondente


class InformacoesModelView(ModelView):  # Crie uma ModelView para Informacoes
    datamodel = SQLAInterface(Informacoes)
    related_views = [AlunoModelView]
    
    label_columns = {'aluno':'Aluno'}
    list_columns = ['id','celular','data_nasc']

    show_fieldsets = [
        (
            'Sumário',
            {'Campos': ['name', 'address', 'aluno']}
        ),
        (
            'Info. Pessoais',
            {'Campos': ['data_nasc', 'celular', 'endereco'], 'expanded': False}
        ),
    ]
    
db.create_all()
appbuilder.add_view(
    AlunoModelView,
    "List Groups",
    icon = "fa-folder-open-o",
    category = "Gestão",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    InformacoesModelView,
    "List Contacts",
    icon = "fa-envelope",
    category = "Gestão"
)