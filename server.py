from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
biodata = [
    {
        "nama": "budi",
        "alamat": "malang"
    },
    {
        "nama": "ananta",
        "alamat": "malang"
    }
]


@app.route("/biodata")
def index():
    return jsonify(biodata)


@app.route("/biodata/<index>")
def show(index):
    return jsonify(biodata[int(index)])


@app.route("/biodata", methods=["POST"])
def store():
    biodata.append(request.json)
    return jsonify({"success": True})


@app.route("/biodata/<index>", methods=["PUT"])
def update(index):
    biodata[int(index)] = request.json
    return jsonify({"success": True})


@app.route("/biodata/<index>", methods=["DELETE"])
def destroy(index):
    del biodata[int(index)]
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run()

