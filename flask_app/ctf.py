import tempfile
import subprocess

from flask import Flask, render_template, url_for, request, jsonify, escape


class Challenge(object):

    def __init__(self, route):
        self.href = url_for(route)
        self.name = ' '.join(w.capitalize() for w in route.split('_'))


challenge_names = {
    "binary_exploit",
    "caeser_cipher",
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

@app.route("/caeser-cipher", methods=("GET",))
def caeser_cipher():
    return render_template("caeser_cipher.html", challenges=get_challenges())

@app.route("/caeser-cipher-check/", methods=("POST",))
def caeser_cipher_check():
    if request.form['plaintext'].upper() == "THEDIEISCAST" or  request.form['plaintext'].upper() == "THE DIE IS CAST":
        return render_template("caeser_cipher.html", challenges=get_challenges(), message="Nice work! You cracked it")
    else:
        return render_template("caeser_cipher.html", challenges=get_challenges(), message="Sorry \"" + request.form['plaintext'] + "\" isn't quite right. Keep trying!")


if __name__ == "__main__":
    app.run()
