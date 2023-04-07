from run import db
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user

# class LoginForm(FlaskForm):
#     username = StringField('username',validators=[InputRequired(),Length(min=4,max=15)],render_kw={"placeholder":"Username"})
#     password = PasswordField('password', validators=[InputRequired(),Length(min=6,max=80)],render_kw={"placeholder":"Password"})
#     submit= SubmitField("Login")
    
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(67))
    password = db.Column(db.String(80))
    loginStatus=db.Column(db.Boolean)

# Contact
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(127))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(80))
    message = db.Column(db.Text)

# Home_Contact
class HomeContact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(127))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(80))
# Login
