
from flask import Blueprint,render_template

from flask import Blueprint,render_template

app_admin= Blueprint('app_admin', __name__)

@app_admin.route('/')
def admin():
    return render_template("admin-dashboard.html")