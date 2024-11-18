from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///desafio_final.db'
app.config['SWAGGER'] = {
    'title': 'Documentacao da API',
    'openapi': '3.0.3'
}

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app.controllers.cliente_controller import routes_cliente_controller
from app.controllers.home_controller import routes_home_controller

app.register_blueprint(routes_cliente_controller, url_prefix ='/v1/clientes')
app.register_blueprint(routes_home_controller, url_prefix ='/')
swagger = Swagger(app,template_file='docs/api_docs.yaml')