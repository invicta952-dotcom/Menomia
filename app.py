from flask import Flask
import requests
import memeflask
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('main.html')
