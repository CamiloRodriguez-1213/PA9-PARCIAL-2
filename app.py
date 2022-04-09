from flask import Flask, render_template, request, redirect, flash,jsonify,session
from models import productsModel
from models import signupUser
from models import validationToken
from models.signinUser import User
from models import getProductsTable
from config.database import db
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
        user = User(email=email,password=password)
        if user == True:
            session['user_id'] = 3
            return redirect("/dashboard")
        else:
            flash("Usuario o contraseña incorrectos")
            return render_template("/views/login/signin.html",email=email, password=password) 
    return render_template("/views/login/signin.html")
@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
        
    return render_template("/views/dashboard/dashboard.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method== 'POST':
        nameUser=request.form['name']
        emailUser=request.form['email']
        passwordUser=request.form['password']
        userAuth = signupUser.createuser(nameUser,emailUser,passwordUser)
        if userAuth == True:
            return redirect("/signin")
        else:
            return render_template("/views/login/signup.html", name = nameUser, email = emailUser, passwordUser = passwordUser)
        
    return render_template("/views/login/signup.html")
@app.route("/authToken/<token>", methods=["POST", "GET"])
def authToken(token):
    validationToken.valToken(token)
    return render_template("/views/authEmail/recoveryPass.html")
@app.route("/newProduct", methods=["GET","POST"])
def newProductPost():
    if request.method == 'POST':
        nameProduct = request.form['name_product']
        fileProduct = request.files['imagen']
        fileProduct.save('./static/img'+fileProduct.filename)
        print(nameProduct)
        print(fileProduct)
        return render_template("index.html")
    return render_template("/views/productos/productos.html")
@app.route("/tabla", methods=["POST", "GET"])
def tableProducts():
    if request.method == 'POST':
        insertar = request.form['draw'] 
        fila = int(request.form['start'])
        filaPagina = int(request.form['length'])
        buscarValor = request.form["search[value]"]
        columnaOrd = request.form["order[0][column]"]
        campoOrd = request.form["columns["+columnaOrd+"][data]"]
        ordenDir = request.form["order[0][dir]"]
        response = getProductsTable.getTable(insertar,fila,filaPagina,buscarValor,campoOrd,ordenDir)
        return jsonify(response)
app.run(debug=True)
