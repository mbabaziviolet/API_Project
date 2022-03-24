from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"






























# from fastfood import app
# from flask import jsonify



# @app.route('/')
# def index():
#     return 'hello'


# @app.route("/orders",methods=['GET'])
# def get():
#     return jsonify({'Orders':orders})