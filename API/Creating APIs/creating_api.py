import pandas
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homePage():
    return 'This is my API page'

app.run()