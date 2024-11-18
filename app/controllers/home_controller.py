from app.app import app
from flask import Blueprint, render_template
from app.controllers.cliente_controller import ClienteController

routes_home_controller = Blueprint('home',__name__,template_folder='templates')

class HomeController:
    @routes_home_controller.route('/')
    def home_page():
        return render_template('index.html')
