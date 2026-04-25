# Inkwell — Simple Blog Platform

**Experiment 5 | Flask Web Development Assignment**

---

## Project Overview

Inkwell is a Flask-based blog application supporting full CRUD operations (Create, Read, Update, Delete). Posts are stored in an in-memory Python list — no database required.

---

## Features

| Task | Feature | Status |
|------|---------|--------|
| 1 | Project structure: app.py, templates/, static/ with comments | ✅ |
| 2 | Flask app init, home route `/`, in-memory post storage | ✅ |
| 3 | `/create` route — form to add new posts | ✅ |
| 4 | Home page lists all posts with title, excerpt, date | ✅ |
| 5 | `/edit/<id>` route — pre-filled edit form, saves changes | ✅ |
| 6 | `/delete/<id>` route — removes post, redirects home | ✅ |
| 7 | Bonus — CSS styling, sticky nav bar, responsive layout | ✅ |

---

## File Structure

```
simple_blog/
├── app.py                  ← Flask routes and logic
├── requirements.txt        ← Python dependencies
├── README.md
├── templates/
│   ├── base.html           ← Master layout (nav, footer)
│   ├── index.html          ← Home page (post listing)
│   ├── create.html         ← New post form
│   └── edit.html           ← Edit post form
└── static/
    └── style.css           ← All styles
```

---

## How to Run

### Step 1 — Extract the zip
Unzip `simple_blog.zip` and open the `simple_blog` folder in VS Code.

### Step 2 — Install Flask
Open the VS Code Terminal (`Ctrl + ~`) and run:
```bash
pip install flask
```
Or using the requirements file:
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
Visit: **http://127.0.0.1:5000**

Press `Ctrl + C` in the terminal to stop the server.

---

## External References

- Flask documentation: https://flask.palletsprojects.com
- Jinja2 templating: https://jinja.palletsprojects.com
- All code written originally for this assignment.

---

## Academic Integrity

This project is original work created individually for Experiment 5. No code was copied from peers or online repositories.
