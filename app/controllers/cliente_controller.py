from flask import jsonify, Blueprint,request,Response
from app.models.cliente import Cliente
from app.services.cliente_service import ClienteService

routes_cliente_controller = Blueprint('clientes',__name__,template_folder='templates')

class ClienteController:
    @routes_cliente_controller.route('/',methods = ['GET'])
    def listar_todos():
        return jsonify(ClienteService.listar_todos())
    
    @routes_cliente_controller.route('/',methods = ['POST'])
    def salvar_via_json(): 
        nome = request.json.get('nome')
        email = request.json.get('email')
        cliente = Cliente(nome,email)
        return jsonify(ClienteService.salvar(cliente))
    
    @routes_cliente_controller.route('/',methods = ['PUT'])
    def atualizar_cliente():
        nome_atualizado = request.json.get('nome')
        email_atualizado = request.json.get('email')
        id_cliente = request.json.get('id')
        return jsonify(ClienteService.atualizar(id_cliente, nome_atualizado, email_atualizado))
    
    @routes_cliente_controller.route('/insert_form',methods = ['POST'])
    def salvar_via_form(): 
        nome = request.form.get('nome')
        email = request.form.get('email')
        cliente = Cliente(nome,email)
        return jsonify(ClienteService.salvar(cliente))
    
    @routes_cliente_controller.route('/contar')
    def contar_clientes():
        #processar a resposta e direcionar conforme json?
        return jsonify(ClienteService.contar_clientes())
    
    @routes_cliente_controller.route('/delete_form',methods = ['POST'])
    def deletar_via_form():
        id=request.form.get('id')
        return Response(ClienteService.deletar(id), status=200)
    
    @routes_cliente_controller.route('/<id>',methods = ['GET'])
    def buscar_por_id(id:int):
        #processar a resposta e direcionar conforme
        return jsonify(ClienteService.buscar_por_id(id))
    
    @routes_cliente_controller.route('/<id>',methods = ['DELETE'])
    def deletar_por_id(id:int):
        #processar a resposta e direcionar conforme
        return Response(ClienteService.deletar(id),status=200)
    
    @routes_cliente_controller.route('/<id>',methods = ['POST'])
    def atualiza_via_form(id:int):
        nome_atualizado = request.form.get('nome')
        email_atualizado = request.form.get('email')
        return jsonify(ClienteService.atualizar(id, nome_atualizado, email_atualizado))
    
    @routes_cliente_controller.route('/nome/<nome>',methods = ['GET'])
    def buscar_por_nome(nome:str):
        #processar a resposta e direcionar conforme
        return jsonify(ClienteService.buscar_por_nome(nome))
