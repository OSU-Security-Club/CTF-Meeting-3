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
    "cbc"
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
    secrets = open('caeser-cipher-keys.txt', 'r').readlines()
    return render_template("caeser_cipher.html", challenges=get_challenges(), ciphertext=secrets[1])

@app.route("/caeser-cipher", methods=("POST",))
def caeser_cipher_check():
    secrets = open('caeser-cipher-keys.txt', 'r').readlines()

    attempt = request.form['plaintext'].strip().replace(' ', '').upper()
    key = secrets[0].strip().replace(' ', '').upper()

    if attempt == key:
        return render_template("caeser_cipher.html", challenges=get_challenges(), ciphertext=secrets[1], message="Nice work! You cracked it")
    else:
        return render_template("caeser_cipher.html", challenges=get_challenges(), ciphertext=secrets[1], message="Sorry \"" + request.form['plaintext'] + "\" isn't quite right. Keep trying!")

@app.route("/cbc", methods=("GET",))
def cbc():
    return render_template("cbc.html", challenges=get_challenges())

if __name__ == "__main__":
    app.run()
