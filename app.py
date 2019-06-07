from random import randint

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from lidarproc.main.data_retrieval import LidarThread


app = Flask(__name__, static_folder='flaskvue/dist/static', template_folder='flaskvue/dist')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/connect-lidar', methods=["POST"])
def connect_lidar():
    if request.method == "POST":
        address = request.form["address"]
        port = request.form["port"]
        lt = LidarThread("lidar_logger")


if __name__ == '__main__':
    app.run(debug=True)
