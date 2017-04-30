import tempfile
import subprocess

from flask import Flask, render_template, url_for, request, jsonify, escape


class Challenge(object):

    def __init__(self, route):
        self.href = url_for(route)
        self.name = ' '.join(w.capitalize() for w in route.split('_'))


challenge_names = {
    "binary_exploit",
}

app = Flask(__name__)


def get_challenges():
    return [Challenge(name) for name in challenge_names]


@app.route("/")
def home():
    return render_template("home.html", challenges=get_challenges())


@app.route("/binary-exploit", methods=("GET",))
def binary_exploit():
    return render_template("binary_exploit.html", challenges=get_challenges())


if __name__ == "__main__":
    app.run()
