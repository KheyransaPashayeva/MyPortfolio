from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user,login_manager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = '_4#y2L"F4Q8z/n/xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_SECRET_KEY'] = '123232'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="admin_index"


from app.routes import *
from admin.routes import *
from models import *
if __name__ =='__main__':
    # db.create_all()
    app.run(debug=True)