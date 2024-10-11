from flask_appbuilder import ModelView, AppBuilder
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import  CadastroAluno, Escola
from app import db, appbuilder


class InformacoesModelView(ModelView):
    datamodel = SQLAInterface(CadastroAluno)

    label_columns = {'aluno': 'Aluno'}
    list_columns = ['id', 'nome', 'celular', 'data_nasc'] 

    show_fieldsets = [
        (
            'Sumário',
            {'fields': ['nome', 'endereco', 'aluno']}  
        ),
        (
            'Informações Pessoais',
            {'fields': ['data_nasc', 'celular', 'telefone'], 'expanded': False}  
        ),
    ]

class EscolaModelView(ModelView):
    datamodel = SQLAInterface(Escola)

    label_columns = {'nome': 'Nome da Escola', 'endereco': 'Endereço', 'telefone': 'Telefone'}
    list_columns = ['id', 'nome', 'endereco', 'telefone']

    show_fieldsets = [
        (
            'Informações da Escola',
            {'fields': ['nome', 'endereco', 'telefone']}
        ),
    ]

db.create_all()



appbuilder.add_view(
    InformacoesModelView,
    "Cadastrar Alunos",  
    icon="fa-envelope",
    category="Gestão"
)

appbuilder.add_view(
    EscolaModelView,
    "Cadastrar Escolas",  
    icon="fa-building",  
    category="Gestão",
    category_icon="fa-envelope"
)