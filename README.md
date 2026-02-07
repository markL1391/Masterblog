# Flask Blog Application

A minimal blog application built with **Flask** that supports creating, reading, updating, deleting and liking blog posts. 
All data is stored persistently in a local JSON file.

---

## Features

- Display all blog posts on the home page
- Add new blog posts via a form
- Edit existing blog posts
- Delete blog posts
- Like blog posts (persistent like counter)
- Data persistence using a JSON file
- Simple, minimal Scandinavian-inspired UI

---

## Project Structure
```
├── app.py
├── posts.json
├── templates/
│ ├── index.html
│ ├── add.html
│ └── update.html
└── static/
    └── style.css
```
___

## Data Storage

Blog posts are stored in `posts.json` using the following structure:

```json
{
  "id": 1,
  "author": "Author Name",
  "title": "Post title",
  "content": "Post content",
  "likes": 0
}
```

---

## Routes Overview
| Route               | Method    | Description                |
| ------------------- | --------- | -------------------------- |
| `/`                 | GET       | Display all blog posts     |
| `/add`              | GET, POST | Create a new blog post     |
| `/update/<post_id>` | GET, POST | Edit an existing blog post |
| `/delete/<post_id>` | GET       | Delete a blog post         |
| `/like/<post_id>`   | GET       | Increase like counter      |

## How to Run the Application

1. Create and activate a virtual environment (optional but recommended)

2. Install Flask

```bash
pip install flask
```

3. Start the application

```bash
python app.py
```

4. Open your browser and navigate to:

```bash
http://localhost:5001
```
___

## Notes

- This project uses GET requests for delete and like actions for simplicity.
- In production environments, these actions should be handled via POST requests and protected accordingly.
- The application automatically ensures backward compatibility by adding missing fields (e.g. likes) when loading posts.

___

## Author

Mark  
Created as part of a Flask learning project.