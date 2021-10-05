from flask import Flask, render_template

app = Flask(__name__)
prestamos = [8,7,5,2,1,4,56,3,78]
@app.route('/')
def inicio():
    return render_template("index.html", cant_prestamos = len(prestamos)) 
    
@app.route("/addusuario/", methods=["GET", "POST"])
def add_usuario():
    return render_template("formusuario.html")