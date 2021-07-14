from flask import Flask, jsonify
from .get_currency import get_needed_currency


app = Flask(__name__)



@app.route('/')
def index():
    response = jsonify(get_needed_currency())
    return response


