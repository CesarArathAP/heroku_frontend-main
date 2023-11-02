from flask import Flask
from fastapi.middleware.cors import CORSMiddleware
from flask import render_template

app = Flask(__name__)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.route("/")
def index():
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/buscar")
def buscar():
    return render_template('buscar.html')