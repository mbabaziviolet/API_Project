from flask import (Blueprint)
from flask import request ,redirect, render_template,url_for,flash
from werkzeug.security import check_password_hash, generate_password_hash



from fastfood.db import get_db
bp =Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register',methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        contact = request.form['contact']
        password = request.form['password']
        
        db = get_db()
        error = None

        if not name:
            error = 'name is required.'
        if not email:
            error = 'email is required.'
        if not address:
            error = 'address is required.'
        if not contact:
            error = 'contact is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (name, email,address,contact,password) VALUES (?, ?,?,?,?)"),
                
                (name,email,address,contact, generate_password_hash(password)),
                
                db.commit()
            except db.IntegrityError:
             error = f"User {name} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login',methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
    
@bp.route('/logout')
def logout():
    return 'Log out'




