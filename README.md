# Swede Sauna — Flask Website

A full website for **Swede Sauna**, a wood-fired barrel sauna at Robert's Cove beach, West Cork.

## Project Structure

```
swede-sauna/
├── app.py                  # Flask app — routes & data
├── requirements.txt
├── templates/
│   └── index.html          # Jinja2 template (single-page)
└── static/
    ├── css/
    │   └── style.css       # All styles
    └── js/
        └── main.js         # Steam particles, FAQ, form, nav
```

## Setup & Run

```bash
# 1. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dev server
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

## Customise

| What | Where |
|------|-------|
| Business data (features, pricing, FAQ) | `app.py` — top-level lists |
| Phone number | `templates/index.html` — `<a href="tel:...">` |
| Social links | `templates/index.html` — footer social links |
| Colours / fonts | `static/css/style.css` — `:root` variables |
| Contact form backend | `app.py` — `/api/contact` route |

## Production

For deployment (e.g. Render, Railway, Heroku), add **gunicorn**:

```bash
pip install gunicorn
gunicorn app:app
```
