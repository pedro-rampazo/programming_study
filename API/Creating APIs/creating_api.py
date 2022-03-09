import json
import pandas
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homePage():
    return 'This is my API page'


@app.route('/get_ages')
def getAges():
    table = pandas.read_csv('database_api.csv')
    sum_age = sum(table['Age'])
    answer = {'Sum Age': sum_age}
    return jsonify(answer)
