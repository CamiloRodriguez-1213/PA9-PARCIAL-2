from flask import Flask, flash, redirect,render_template,request,session,url_for
from controllers.verifyLog import verifyLogin
from controllers.restorePassword import restpass
from controllers.newPassword import changePassword
from controllers import uploadImage,showImages,validateIdToken,loginUser,editImageController

app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'
@app.route("/", methods=["GET", "POST"])
def index():
    images = showImages.showImages()
    print(images)
    return render_template("index.html",images=images)
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if verifyLogin():
        images = showImages.showImagesUser()
        return render_template("/views/dashboard/dashboard.html",images=images)
    else:
        return redirect("signin")
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        if loginUser.signin(email,password) == True:
            return redirect("/")
        else:
            return render_template("/views/login/signin.html",email=email)
    return render_template("/views/login/signin.html")
@app.route("/authToken/<token>", methods=["GET", "POST"])
def authToken(token):
    if validateIdToken.valToken(token) == True:
        return redirect("/")
    return render_template("/components/alerts/alert.html")
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        if loginUser.signUp(name,email,password) == True:
            return redirect("/")
        else:
            return render_template("/views/login/signup.html",email=email)
    return render_template("/views/login/signup.html")
@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for('signin'))
@app.route("/restorePassword", methods=["GET", "POST"])
def restorePassword():
    if request.method== 'POST':
        email=request.form['email']
        if restpass(email):
            return render_template("/components/alerts/alert.html")
    return render_template("/views/login/restorePassword.html")
@app.get("/newPassword/<id>/<token>")
def newPassword(id,token):
    if validateIdToken.validate(id,token)==True:
        return render_template("/views/login/newPassword.html",id=id,token=token)
    else:
        return render_template("/components/alerts/alert.html")

@app.post("/newPassword")
def sendNewPassword():
    if request.method == 'POST':
        passwordUser=request.form['password']
        id=request.form['id']
        if validateIdToken.validateToken(id):
            changePassword(id,passwordUser)
        else:
            return render_template("/components/alerts/alert.html")
    return redirect("/signin")

@app.route("/uploadImage", methods=["GET","POST"])
def newUpload():
    if request.method == 'POST':
        nameProduct = request.form['name_product']
        fileProduct = request.files['imagen']
        uploadImage.uploadImage(nameProduct,fileProduct)
    return render_template("/views/products/formUploadImage.html")

@app.get("/editImage/<id>")
def editImage(id):
    images = showImages.showImagesEdit(id)
    return render_template("/views/products/formEditImage.html",images=images)

@app.post("/editImage/")
def editImagePost():
    if request.method == 'POST':
        
        id = request.form['id']
        nameProduct = request.form['name_product']
        fileProduct = request.files['imagen']
        editImageController.editImage(nameProduct,fileProduct,id)
    return redirect(url_for('dashboard'))

@app.route("/deleteImage/<id>", methods=["GET","POST"])
def deleteImage(id):
    editImageController.deleteImageUser(id)
    return redirect(url_for('dashboard'))

@app.get("/changeStatus/<id>")
def changeStatus(id):
    editImageController.changeImageStatus(id)
    return redirect(url_for('dashboard'))
app.run(debug=True)