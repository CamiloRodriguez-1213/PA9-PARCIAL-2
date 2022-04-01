from flask import Flask, render_template, request, redirect, flash
import mysql.connector as mysql
from werkzeug.security import generate_password_hash, check_password_hash
from models import productsModel
from models import newUser
from models import signinUser
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = productsModel.obtenerProductos()
    return render_template("index.html",results=results)
@app.route("/signin", methods=["GET","POST"])
def signin():
    result = ''
    if request.method== 'POST':
        email=request.form['email']
        password=request.form['password']
        password=generate_password_hash(password)
        result = signinUser.signUser(email=email,password=password)
    if result =='':
        return render_template("/views/login/signin.html")
    else:
        return redirect("/dashboard")
        
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("/views/dashboard/dashboard.html")
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method== 'POST':
        isvalid = True
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        password=generate_password_hash(password)
        
        if name == '':
            isvalid = False
            flash('El nombre es obligatorio')
            
        if email == '':
            isvalid = False
            flash('El email es obligatorio')
        if password == '':
            isvalid = False
            flash('La contraseña es obligatoria')
        if isvalid == False:
            return render_template("/views/login/signup.html")
        else:
            print(password)
            newUser.createuser(name=name,email=email,password=password)
            return redirect('/signin')
    return render_template("/views/login/signup.html")
    
app.run(debug=True)
