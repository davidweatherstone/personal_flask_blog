from collections import OrderedDict
import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from posts import POSTS

sorted_posts = OrderedDict(sorted(POSTS.items(), reverse=True))

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('FLASK_KEY')
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html", posts=sorted_posts)


@app.route("/post/<int:post_id>", methods=["GET"])
def post(post_id):
    post = POSTS[post_id]
    if post["type"] == "App":
        return render_template("post_iframe.html", post=post)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True, port=5001) 