from flask import Flask, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
import re
from models import productsModel
from models import newUser
from models import signinUser
app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'

@app.route("/", methods=["GET", "POST"])
def index():
    results = productsModel.obtenerProductos()
    
    return render_template("index.html",results=results)

@app.route("/signin", methods=["GET","POST"])
def signin():
    if request.method== 'POST':
        email=request.form['email']
        password=request.form['password']
        passwordCod=generate_password_hash(password)
        user = signinUser.User(email=email,passwordCod=passwordCod)
        return redirect("/dashboard")
    return render_template("/views/login/signin.html")    
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    
    return render_template("/views/dashboard/dashboard.html")
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method== 'POST':
        isValid = True
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        patternpw=re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}')
        passwordval = re.search(patternpw, password)
        
        if name == '':
            isValid = False
            flash('* Nombre')
        if email == '':
            isValid = False
            flash('* Email')
        if not passwordval or password=='':
            isValid = False
            flash('* Contraseña:')
            flash('El campo contraseña debe contener un mínimo de 8 caracteres, un máximo de 20, letras, (minúsculas y MAYÚSCULAS) y Números')
        if isValid == False:
            return render_template("/views/login/signup.html", name = name, email = email)
        else:
            password=generate_password_hash(password)
            newUser.createuser(name=name,email=email,password=password)
            
    return render_template("/views/login/signup.html")
    
app.run(debug=True)
