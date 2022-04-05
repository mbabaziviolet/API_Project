from flask import (Blueprint)
from flask import request ,redirect, render_template,url_for,flash,session,g,jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators

from fastfood.db.db import conn
import psycopg2.extras

from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import unset_jwt_cookies, create_access_token,create_refresh_token,jwt_required,get_jwt_identity,jwt_manager

bp =Blueprint('auth', __name__, url_prefix='/auth')
#Opening a cursor to perform database operations
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


@bp.route('/register', methods= ['POST','GET'])
def register():
  
  if request.method == "POST":
        name = request.json["cst_name"]
        email = request.json["cst_email"]
        address = request.json["cst_address"]
        contact = request.json["cst_contact"]
        password = request.json["cst_password"]
        password2 = request.json["cst_password2"]
        
        
        
        #checking if cst_email exists
        email_exists = cur.execute("SELECT cst_email FROM customers WHERE cst_email = %(cst_email)s", {'cst_email':email})
        if email_exists:
              return jsonify({'error':'Email  already exists!'})
          
         #checking if cst_name exists
        name_exists = cur.execute("SELECT  cst_name FROM customers WHERE cst_name = %(cst_name)s", {'cst_name':name})
        if name_exists:
              return jsonify({'error':'name already in use!'})      
          
          
       #checking ifcst_ address exists
        address_exists = cur.execute("SELECT cst_address FROM customers WHERE cst_address = %(cst_address)s", {'cst_address':address})
        if address_exists:
              jsonify({'error':'Phone number already in use!'}) 
              
        #checking if cst_contact exists
        contact_exists = cur.execute("SELECT cst_contact FROM customers WHERE cst_contact = %(cst_contact)s", {'cst_contact':contact})
        if contact_exists:
              jsonify({'error':'Contact already in use!'})     
        #do passwords match
        if password!=password2:
              jsonify({'error':"Passwords don\t match!"})
        
        if len(password) < 5:
          jsonify({"error":"Password is too short"})  
        
     
        if name.isalpha():
          jsonify({'error':'name must be alphabetic'})  
          
         #validatind the cst_email
        if not validators.email(email):
          jsonify({'error':'Please enter a valid email address'})      
        
        #creating a hashed password in the database
        hashed_password = generate_password_hash(password,method="sha256")
        
        #inserting values
        cur.execute("INSERT INTO customers (cst_name,cst_email,cst_address,cst_contact,cst_password) VALUES (%s,%s,%s,%s,%s)", (name,email,address,contact,hashed_password))
        conn.commit()
      
        return jsonify({'message':'new user created','cst_name':name,'cst_email':email,'cst_address':address,'cst_contact':contact,'password':hashed_password})
  return jsonify({'error':'wrong credentials'}) 







@bp.route('/login', methods= ['POST','GET'])

def login():
      
          email = request.json['cst_email']
          password = request.json['cst_password']
          
          #checking if cst_email exits
          cur.execute('SELECT * FROM customers WHERE cst_email = %(cst_email)s',{'cst_email':email})
          customers = cur.fetchone()
          if customers:
                #checking if cst_password matches the sha password in database
                password_check = check_password_hash(customers['cst_password'],password)
                print(password_check)
                if password_check:
                      # creating access tokens
                      access_token = create_access_token(identity=customers['cst_id'], fresh=True)
                      
                      print(access_token)
                    
                      
                    
                      flash('You have logged in successfully!','success')
                  
                
                      return jsonify({'message':" You logged in successfully!",'access_token':access_token,'cst_email':customers['cst_email'],'cst_id':customers['cst_id']})
                
                
          return jsonify({'error':'customers doesnt exists'})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















