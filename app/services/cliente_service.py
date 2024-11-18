from app.models.cliente import Cliente
from app.repository.cliente_repository import ClienteRepository

class ClienteService:
    def listar_todos():
        return ClienteRepository.listar_todos()
    
    def buscar_por_id(id:int):
        return ClienteRepository.buscar_por_id(id)
    
    def buscar_por_nome(nome:str):
        return ClienteRepository.buscar_por_nome(nome)
    
    def contar_clientes():
        return ClienteRepository.total_registros()
    
    def salvar(cliente:Cliente):     
        return ClienteRepository.salvar_cliente(cliente)
    
    def deletar(id):
        return ClienteRepository.deletar_por_id(id)
    
    def atualizar(id_cliente:int, nome_atualizado:str, email_atualizado:str):
        return ClienteRepository.atualizar_cliente(id_cliente, nome_atualizado, email_atualizado)
    