import json
from flask import Flask

app = Flask(__name__)

POSTS_FILE = "posts.json"

@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)