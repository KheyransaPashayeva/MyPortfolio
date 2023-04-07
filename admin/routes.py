#  admin/routes
from run import app,db
from flask import render_template, request,url_for,redirect
import os
from werkzeug.utils import redirect
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user,login_manager
from run import login_manager


@login_manager.user_loader
# burda def adi load_user olmalidir
def load_user(user_id):
    from models import User
    return User.query.get(user_id)


@app.route('/login', methods=["GET", "POST"])
def admin_index():
    from models import User
    from run import db
    login = User(
        username = "xeyrense",
        password = "salam!@#123",
        loginStatus=False
    )
    db.session.add(login)
    db.session.commit()

    if request.method=="POST":
        if login.username == request.form['username'] and login.password == request.form['password']:
            login_user(login)
            return redirect (url_for("base"))
        else:
            return redirect(url_for("admin_index"))
    return render_template("admin/login.html", login=login)

@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for("admin_index"))

@app.route("/admin",methods=["GET","POST"])
@login_required
def base():
    return render_template("admin/base.html")

# Contact
@app.route('/admin/contact', methods=['GET', 'POST'])
@login_required
def admin_contact():
    from models import Contact
    messages=Contact.query.all()
    if request.method == 'POST':
        firstname = request.form['firstname']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']
        contact=Contact(
            full_name = firstname,
            phone = phone,
            email= email,
            message = message
        )
        db.session.add(contact)
        db.session.commit()
        return redirect('/contact')

    return render_template('admin/contact.html',message = messages)

@app.route('/admin/contact/delete/<int:id>')
@login_required
def admin_contact_delete(id):
    from models import Contact
    messages=Contact.query.filter_by(id=id).first()
    db.session.delete(messages)
    db.session.commit()
    return redirect('/admin/contact')

    # HomeContact 

@app.route('/admin/home_contact', methods=['GET', 'POST'])
@login_required
def homecontact():
    from models import HomeContact
    email=HomeContact.query.all()
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        home_contact=HomeContact(
            first_name = firstname,
            lastname = lastname,
            email= email,
        )
        db.session.add(home_contact)
        db.session.commit()
        return redirect('/')

    return render_template('admin/home_contact.html',message = email)

@app.route('/admin/home_contact/delete/<int:id>')
@login_required
def admin_homecontact_delete(id):
    from models import HomeContact
    messages=HomeContact.query.filter_by(id=id).first()
    db.session.delete(messages)
    db.session.commit()
    return redirect('/admin/home_contact')