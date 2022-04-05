from unicodedata import name
from flask import Blueprint
from flask import request, render_template,flash,session,g
from fastfood.db.db import conn
import psycopg2.extras
from flask import flash, jsonify, redirect, render_template, request, url_for
import psycopg2.extras
from flask_jwt_extended import jwt_required,get_jwt_identity


cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # Check if user is loggedin
    #if 'loggedin' in session:
    
        # User is loggedin show them the home page
    return render_template('home.html')
    # User is not loggedin redirect to login page
    
@views.route('/orders', methods=['GET','POST'])
def orders():

     return render_template('orders.html')


@views.route("/menu", methods=['GET'])
def all_menu_product():


    cur.execute("SELECT * FROM product")
    products = cur.fetchall()

    return jsonify({'menu':products})



@views.route("/menu/<int:id>", methods=['GET'])
def menu_products_(product_id):
    cur.execute('SELECT * FROM product WHERE product_id = %(product_id)s',{'product_id':id})
    data = cur.fetchone()
    
    return jsonify({'id':data['id'],'name':data['food_name'],'price':data['food_price'],'description':data['food_description'],'stock':data['food_stock_quantity']})


@views.route("/menu/create", methods=['GET',"POST"])
@jwt_required()
def new_menu_product():
    if request.method == "POST":
        product_name = request.json['product_name']
        product_price = request.json['product_price']
        product_description = request.json['product_description']
        product_image_url = request.json['product_image_url']
       
    
        cur.execute("INSERT INTO product (product_name,product_price,product_description,product_image_url) VALUES (%s,%s,%s,%s)", (product_name,product_price,product_description,product_image_url))
        conn.commit()
        flash("New menu product added successfully!!",'success')
        return redirect(url_for('admin.route'))
    
    
    return jsonify({'message':'new product item created','product name':product_name,'poduct price':product_price,'food description':product_description})





