from flask import Flask, render_template, abort
from jinja2.exceptions import TemplateNotFound


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/<page>")
def page(page):
    try:
        return render_template(f"{page}.html")
    except TemplateNotFound:
        abort(404)
