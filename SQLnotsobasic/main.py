from flask import Flask, request, render_template, redirect, url_for, abort
from connection import database_handler, write_to_database

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
