from app.app import db
from app.models.cliente import Cliente

class ClienteRepository:
    def salvar_cliente(cliente:Cliente):
        """Salva o cliente fornecido e retorna sua entrada no banco de dados."""
        db.session.add(cliente)
        db.session.commit()
        id_inserido = cliente.id
        return ClienteRepository.buscar_por_id(id_inserido)

    def deletar(obj):
        """Deleta o objeto fornecido"""
        db.session.delete(obj)
        db.session.commit()

    def deletar_por_id(id:int):
        """Encontra o objeto pelo ID e então o deleta"""
        obj = ClienteRepository.buscar_por_id(id)
        ClienteRepository.deletar(obj)
    
    def listar_todos():
        """Retorna toda as entradas do banco de dados como uma lista de objetos Cliente"""
        return db.session.scalars(db.select(Cliente).order_by(Cliente.id)).all()
    
    def buscar_por_id(id:int):
        """Busca o objeto identificado pelo id, disparando uma exceção caso seja encontrado mais de um resultado."""
        return db.one_or_404(db.select(Cliente).filter_by(id=id),description=f'Nenhum cliente com o id {id} presente na base de dados.')
    
    def buscar_por_nome(nome:str):
        """Retorna lista contendo todas as entradas do banco de dados cujo nome corresponde ao nome fornecido"""
        return db.session.scalars(db.select(Cliente).filter_by(nome=nome)).all()
    
    def total_registros():
        """Retorna a contagem do total de registros"""
        return db.session.query(Cliente.id).count()
    
    def atualizar_cliente(id_cliente, nome_atualizado, email_atualizado):
        """Atualiza o cliente com o id fornecido com os dados fornecidos"""
        cliente = ClienteRepository.buscar_por_id(id_cliente)
        cliente.nome = nome_atualizado
        cliente.email = email_atualizado
        db.session.commit()
        return ClienteRepository.buscar_por_id(id_cliente)