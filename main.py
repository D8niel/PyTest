#! /usr/bin/python3

__production__ = False

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello there from Flask!'


if __name__ == "__main__":
    if __production__:
        from waitress import serve
        serve(app, host='0.0.0.0', port=80)
    else:
        app.run(debug=True)
