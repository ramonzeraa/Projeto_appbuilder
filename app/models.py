from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Aluno(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    matricula = Column(String(20), unique = True, nullable=False)

    def __repr__(self):
        return self.name
    
class Contact(Model):
    id = Column(Integer, primary_key=True)
    nome =  Column(String(150), unique = True, nullable=False)
    enredeco =  Column(String(564), default='Street ')
    data_nasc = Column(Date)
    telefone = Column(String(20))
    celular = Column(String(20))
    aluno_id = Column(Integer, ForeignKey('aluno.id'))
    aluno = relationship("Aluno")

    def __repr__(self):
        return self.name