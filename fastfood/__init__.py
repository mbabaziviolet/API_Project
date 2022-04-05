import imp
from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'joy2'
    
    
    from .auth import auth
    from .index import views

    #from .food.items import menu
    # from .admin.route import app_admin
    #from fastfood.profile.profile import pro_file
    #app.static_folder= 'static'
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(views.views)
    
    #app.register_blueprint(items.menu)
    #app.register_blueprint(app_admin)
    #app.register_blueprint(pro_file)
    
    JWTManager(app)

 
    return app
