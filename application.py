import functions as f
from flask import Flask, jsonify, request
from models import Base
from session import engine

application = Flask(__name__)
data = f.load_file('./heroes.csv')
Base.metadata.create_all(engine)


@application.route("/")
def index():
    return jsonify(data)

@application.route("/email/add", methods = ['POST'])
def add_email():
    ip = request.remote_addr
    data = f.add_email(request.get_json(),ip)
    return jsonify(data)

@application.route("/<string:id>")
def heroe(id):
    return jsonify(data[id])

if __name__ == "__main__":
    application.run(port = 5000, debug = True)