# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
import json

try:
    import api  # type: ignore
except ModuleNotFoundError:
    from ktc import api  # type: ignore


app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "PUT"])
def home():
    return render_template("index.html")


@app.route("/api/environments", methods=["GET"])
def get_environments():
    return jsonify(api.get_list_of_environments())


@app.route("/api/sizes", methods=["GET"])
def get_sizes():
    return jsonify(api.get_list_of_sizes())


@app.route("/api/crs", methods=["GET"])
def get_crs():
    return jsonify(api.get_list_of_challenge_ratings())


@app.route("/api/sources", methods=["GET"])
def get_sources():
    return jsonify(api.get_list_of_sources())


@app.route("/api/types", methods=["GET"])
def get_types():
    return jsonify(api.get_list_of_monster_types())


@app.route("/api/alignments", methods=["GET"])
def get_alignments():
    return jsonify(api.get_list_of_alignments())


@app.route("/api/monsters", methods=["GET", "POST"])
def get_monsters():
    print(request.form)
    try:
        monster_parameters_string = request.values["params"]
        print(monster_parameters_string)
        monster_parameters = json.loads(monster_parameters_string.replace("'", '"'))
    except:
        monster_parameters = {}
    print(monster_parameters)
    return jsonify(api.get_list_of_monsters(monster_parameters))


if __name__ == "__main__":
    app.run(debug=True)
