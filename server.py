import os
from pathlib import Path
from bottle import Bottle


def index():
    return Path("index.html").read_text()


def create_app():
    app = Bottle()
    app.route("/", "GET", index)
    return app


application = create_app()
application.run()
