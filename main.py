from flask import Flask, make_response, jsonify, request
from bd import Names

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # this is to organize the response in the POST method!


@app.route("/names", methods=["GET"])
def get_names():
    return make_response(jsonify(
        Title='data list.',
        data=Names)
    )


@app.route("/names", methods=["POST"])
def create_name():
    names = request.json
    Names.append(names)  # It's for add to the list
    return make_response(
        jsonify(
            Return="successfully registered data .",
            data=names)
    )
    return names


app.run(port=8080, host="localhost", debug=True)
