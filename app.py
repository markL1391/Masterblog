import json
from json import JSONDecodeError

from flask import Flask, render_template

app = Flask(__name__)

POSTS_FILE = "posts.json"

def load_posts():
    try:
        with open("posts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)