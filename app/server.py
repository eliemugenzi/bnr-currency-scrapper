from flask import Flask, jsonify, request
import json
from .get_currency import get_needed_currency


app = Flask(__name__)



@app.route('/')
def index():
    response = jsonify(get_needed_currency())
    return response


@app.route('/pindo', methods=['POST'])
def pindo_callback():
    body = request.data

    cc = json.loads(body)
    print('CC', cc)

    return cc
