import json
from json import JSONDecodeError
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# JSON file that stores all blog posts.
POSTS_FILE = "posts.json"

def load_posts():
    """
    Load all blog posts from JSON file.
    Returns an empty list if the file does not exist
    or contains invalid JSON (Error Handling).
    """
    try:
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            posts = json.load(f)

        # Add likes if missing.
        for post in posts:
            post.setdefault("likes", 0)
        return posts

    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []


def save_posts(posts):
    """
    Save the given list of blog posts to the JSON file.
    """
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


def fetch_post_by_id(posts, post_id):
    """Return the post with the given ID, or None if not found.
    """
    for post in posts:
        if post.get("id") == post_id:
            return post
    return None


@app.route('/')
def index():
    """
    Start page (Home route).
    Displays all blog posts loaded from the JSON file.
    """
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Add route.
    GET: Display the form to create a new blog post.
    POST: Process the form and save a new blog post.
    """
    if request.method == 'POST':
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Validation: All fields are required.
        if not author or not title or not content:
            return render_template("add.html", error="Please fill in all fields.")

        posts = load_posts()

        # Generate a new unique ID.
        new_id = max([post.get("id", 0) for post in posts], default=0) + 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
            "likes": 0
        }

        posts.append(new_post)
        save_posts(posts)

        # Redirect to home page after successful creation.
        return redirect(url_for("index"))

    # Get request.
    return render_template("add.html")


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Delete route.
    Removes the blog post with the given ID from the JSON file and
    redirects back to the home page.
    """
    posts = load_posts()

    # Keep all posts except the one with the given ID.
    posts = [post for post in posts if post.get("id") != post_id]

    save_posts(posts)

    # Redirect back to the home page.
    return redirect(url_for("index"))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Update route.
    GET: Displays the edit form pre-filled with the current blog post data.
    POST: Updates the blog post with the submitted form data, saves changes
    to the JSON file and redirects to the home page.
    """
    posts = load_posts()

    # Fetch the blog post from the JSON file
    post = fetch_post_by_id(posts, post_id)

    if post is None:
        # Blog post with given ID does not exist.
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Validation: All fields are required.
        if not author or not title or not content:
            return render_template("update.html", post=post, error="Please fill in all fields.")

        # Update the existing post fields.
        post["author"] = author
        post["title"] = title
        post["content"] = content

        # Update the post in the JSON file.
        save_posts(posts)
        # Redirect back to index.
        return redirect(url_for("index"))

    # GET request, displays the update.html page.
    return render_template("update.html", post=post)

@app.route('/like/<int:post_id>')
def like(post_id):
    """
    Like route.
    Increases the like counter of the blog post with the given ID
    and redirects back to the home page.
    """
    posts = load_posts()
    post = fetch_post_by_id(posts, post_id)

    if post is None:
        return "Post not found", 404

    # Increase the like counter by one.
    post["likes"] += 1
    save_posts(posts)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)