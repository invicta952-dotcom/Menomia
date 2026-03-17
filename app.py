from flask import Flask, render_template
import memeflask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")

@app.route("/meme")
def index():
    return render_template("meme_index.html")


