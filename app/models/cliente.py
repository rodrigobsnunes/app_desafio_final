from app.app import db
from dataclasses import dataclass

@dataclass
class Cliente(db.Model):
    id:int = db.Column("id",db.Integer,primary_key=True)
    nome:str = db.Column("nome",db.String(100),nullable=False)
    email:str = db.Column("email",db.String(100),nullable=False)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
