from flask import Flask, render_template
import memeflask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")

@app.route("/meme")
def index():
    meme_pic, subreddit = memeflask.get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


