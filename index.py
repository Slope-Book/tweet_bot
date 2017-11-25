import os
from bottle import route, run

@route("/")
def hello_world():
    return "hello world"

run(host="0.0.0.0", port=int(os.environ.get("POST", 5000)))