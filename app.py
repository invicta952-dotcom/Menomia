from flask import Flask, render_template
import requests
import memeflask
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('main.html')

@app.route('/meme')  # This must match what you typed in the browser
def get_meme():
    # Your logic to get the meme using memeflask.py
    return render_template('meme_index.html', meme_image=meme_url) 


if __name__ == "__main__":
    app.run()

