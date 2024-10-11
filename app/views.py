from flask_appbuilder import ModelView, AppBuilder
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import  CadastroAluno, Escola
from app import db, appbuilder


class InformacoesModelView(ModelView):
    datamodel = SQLAInterface(CadastroAluno)

    label_columns = {'aluno': 'Aluno'}
    list_columns = ['id', 'nome', 'celular', 'data_nasc']  # Adicione 'nome' à lista de colunas

    show_fieldsets = [
        (
            'Sumário',
            {'fields': ['nome', 'endereco', 'aluno']}  # Corrigido 'Campos' para 'fields'
        ),
        (
            'Informações Pessoais',
            {'fields': ['data_nasc', 'celular', 'telefone'], 'expanded': False}  # Ajustado para 'telefone' e 'endereco'
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
# Cria as tabelas no banco de dados
db.create_all()

# Adiciona as views ao app


appbuilder.add_view(
    InformacoesModelView,
    "Cadastrar Alunos",  # Nome alterado para "Listar Informações"
    icon="fa-envelope",
    category="Gestão"
)

appbuilder.add_view(
    EscolaModelView,
    "Cadastrar Escolas",  # Nome da nova view
    icon="fa-building",  # Ícone para a nova view
    category="Gestão",
    category_icon="fa-envelope"
)