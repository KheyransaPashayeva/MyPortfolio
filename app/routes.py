
from run import app,db
from flask import render_template, request,url_for,redirect
import os


@app.route('/')
def index():
    return render_template('app/index.html') 

@app.route('/about')
def about():
    return render_template('app/about.html')

@app.route('/service')
def service():
    return render_template('app/service.html') 

@app.route('/project')
def project():
    return render_template('app/project.html') 

@app.route('/contact')
def contact():
    return render_template('app/contact.html') 


