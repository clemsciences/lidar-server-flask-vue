"""

"""
from random import randint
import json

import aiohttp
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__, static_folder='flaskvue/frontend/static', template_folder='flaskvue/frontend')
# socketio = SocketIO(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

session = aiohttp.ClientSession()


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/connect-lidar', methods=["POST"])
def connect_lidar():
    global address, port
    if request.method == "POST":
        address = request.form["address"]
        port = request.form["port"]


@app.route("/get_measures", methods=["POST"])
async def get_measures():
    async with session.post(address+"/get_measures") as resp:
        return jsonify(await resp.json())


@app.route("/test_measures")
def get_measures_test():
    with open("data/measures_233530092019.json") as f:
        measures = json.load(f)
        return jsonify(measures)


@app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8081)
    session.close()
