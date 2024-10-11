from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from app import db
    
class CadastroAluno(Model):
    id = Column(Integer, primary_key=True)
    nome =  Column(String(150), unique = True, nullable=False)
    enredeco =  Column(String(564), default='Street ')
    data_nasc = Column(Date)
    telefone = Column(String(20))
    celular = Column(String(20))
    Cadastro_aluno_id = Column(Integer, ForeignKey('cadastro_aluno.id'))


    def __repr__(self):
        return self.nome
    
class Escola(Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    telefone = Column(String(20), nullable=True)
    data_fundacao = Column(Date)
    
    def __repr__(self):
        return f"<Escola {self.nome}>"