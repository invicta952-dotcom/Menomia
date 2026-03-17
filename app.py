from flask import Flask
import memeflask
app = Flask(__name__)
@app.route("/")
def index():
    return "index.html"


