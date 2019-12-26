import os
from bottle import Bottle, request, template, static_file
from pathlib import Path


ip_dict = {}


def hello():
    client_ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    if client_ip in ip_dict:
        ip_dict[client_ip] += 1
    else:
        ip_dict[client_ip] = 1
    return template("index.html", ippp=ip_dict)


def html_statics(file_name):
    return static_file(file_name, root="./")


def reader(file):
    return Path(file).read_text()


def create_app():
    app = Bottle()
    app.route("/", "GET", hello)
    app.route("/<file_name:path>", "GET", html_statics)
    app.route("/<file>", "GET", reader)
    return app


application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))