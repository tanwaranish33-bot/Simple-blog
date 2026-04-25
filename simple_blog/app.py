# ============================================================
#  Project Title : Simple Blog Platform
#  Author        : [Your Name]
#  Date          : April 25, 2026
#  Description   : A Flask-based blog application supporting
#                  full CRUD operations (Create, Read, Update,
#                  Delete) for blog posts. Data is stored in
#                  an in-memory list (no database required).
# ============================================================

from flask import Flask, render_template, request, redirect, url_for

# ── App Initialization ────────────────────────────────────────
app = Flask(__name__)

# ── In-Memory Data Store ──────────────────────────────────────
# Each post is a dictionary: { id, title, content, date }
posts = []
next_id = 1  # Auto-incrementing ID counter


def get_post(post_id):
    """Helper: return the post dict matching post_id, or None."""
    return next((p for p in posts if p["id"] == post_id), None)


# ── Seed Sample Posts ─────────────────────────────────────────
# Pre-populate with two example posts so the home page isn't blank.
def seed_posts():
    global next_id
    samples = [
        {
            "title": "Welcome to Simple Blog",
            "content": (
                "This is your first blog post! This platform lets you "
                "create, read, edit, and delete blog posts with ease. "
                "Click 'New Post' in the navigation to get started."
            ),
        },
        {
            "title": "How Flask Works",
            "content": (
                "Flask is a lightweight Python web framework. It maps "
                "URL routes to Python functions, renders HTML templates "
                "using Jinja2, and handles HTTP requests and responses — "
                "all with minimal boilerplate code."
            ),
        },
    ]
    for s in samples:
        from datetime import date
        posts.append({
            "id":      next_id,
            "title":   s["title"],
            "content": s["content"],
            "date":    date.today().strftime("%B %d, %Y"),
        })
        next_id += 1


seed_posts()


# ── Routes ────────────────────────────────────────────────────

# Task 2 & 4 — Home: display all posts
@app.route("/")
def index():
    """Home page — lists all blog posts in reverse-creation order."""
    return render_template("index.html", posts=list(reversed(posts)))


# Task 3 — Create: show form and handle submission
@app.route("/create", methods=["GET", "POST"])
def create():
    """
    GET  → render empty create form
    POST → validate, save new post, redirect home
    """
    global next_id
    error = None

    if request.method == "POST":
        title   = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Server-side validation
        if not title or not content:
            error = "Both title and content are required."
        else:
            from datetime import date
            posts.append({
                "id":      next_id,
                "title":   title,
                "content": content,
                "date":    date.today().strftime("%B %d, %Y"),
            })
            next_id += 1
            return redirect(url_for("index"))

    return render_template("create.html", error=error)


# Task 5 — Update: pre-fill form and save changes
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    """
    GET  → render form pre-filled with existing post data
    POST → validate, update post in-place, redirect home
    """
    post  = get_post(post_id)
    error = None

    if post is None:
        # Post not found — redirect home
        return redirect(url_for("index"))

    if request.method == "POST":
        title   = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not title or not content:
            error = "Both title and content are required."
        else:
            # Update the post in-place
            post["title"]   = title
            post["content"] = content
            return redirect(url_for("index"))

    return render_template("edit.html", post=post, error=error)


# Task 6 — Delete: remove post and redirect
@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    """
    POST only (form submit) — removes the post with the given id
    and redirects the user back to the home page.
    """
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return redirect(url_for("index"))


# ── Entry Point ───────────────────────────────────────────────
if __name__ == "__main__":
    # debug=True enables auto-reload during development
    app.run(debug=True)
