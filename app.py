from flask import Flask, render_template
import memeflask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


