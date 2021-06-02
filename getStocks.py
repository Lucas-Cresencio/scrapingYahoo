import requests
from flask import Flask, request, jsonify

app = Flask("Stocks")

from main import getStock

region = ''

@app.route("/stocks/", methods=["GET"])
def get_stock():
    region = request.args.get('region')
    return getStock(region)

app.run()