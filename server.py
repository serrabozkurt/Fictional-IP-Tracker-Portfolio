import os
from bottle import Bottle, request, template, static_file
from pathlib import Path
from hashlib import sha256


def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


ip_dict = {}


def hello():
    client_ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    if client_ip in ip_dict:
        ip_dict[client_ip] += 1
    else:
        ip_dict.update({client_ip:1})
    return template("index.html", ippp=ip_dict)


def resetter(filename):
    incoming_pwd = request.forms.password
    terms = request.forms.terms
    hashed_entry = create_hash(incoming_pwd)
    while True:
        if hashed_entry == "8e20775010852c6e583e1d0510b50644011ebca66e6930cd14d848926a39070a" and terms == "accepted":
            ip_dict.clear()
            return template('reset.html')
        else:
            return template("wrongpwd.html")


def html_statics(file_name):
    return static_file(file_name, root="./")


def reader(file):
    return Path(file).read_text()


def create_app():
    app = Bottle()
    app.route("/", "GET", hello)
    app.route("/<file_name:path>", "GET", html_statics)
    app.route("/<file>", "GET", reader)
    app.route('/<filename>', 'POST', resetter)
    return app


application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
