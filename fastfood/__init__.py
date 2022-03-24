from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'joy2'
    
    from . import auth
    app.register_blueprint(auth.bp)
    return app
