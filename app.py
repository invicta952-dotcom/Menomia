from flask import Flask, render_template
import requests
import memeflask
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('main.html')

@app.route(/meme)
def meme():
    return render_template('meme_index.html)

if __name__ == "__main__":
    app.run()

