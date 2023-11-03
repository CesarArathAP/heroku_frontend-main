from flask import Flask
from flask import render_template
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

@app.route("/")
def index():
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/buscar")
def buscar():
    return render_template('buscar.html')