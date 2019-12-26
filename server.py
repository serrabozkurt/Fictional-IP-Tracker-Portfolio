import os
from bottle import Bottle, request, template


ip_dict = {}


def hello():
    client_ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    if client_ip in ip_dict:
        ip_dict[client_ip] += 1
    else:
        ip_dict[client_ip] = 1
    return template("index.html", ippp=ip_dict)



def create_app():
    app = Bottle()
    app.route("/", "GET", hello)
    return app


application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))