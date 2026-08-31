from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)


@app.context_processor
def inject_has_image():
    def has_image(path):
        return os.path.isfile(os.path.join(app.static_folder, path))
    return {"has_image": has_image}

BOOKWHEN_URL = "https://bookwhen.com/swedesauna"
REVOLUT_URL  = "https://revolut.me/saraufd3v"

NAV = [
    {"label": "Home", "url": "/"},
    {"label": "Events", "url": "/events"},
    {"label": "Shop",   "url": "/shop"},
    {"label": "About",  "url": "/about"},
]

SESSIONS = [
    {"duration": "30", "unit": "min", "price": "15", "desc": "A focused reset"},
    {"duration": "60", "unit": "min", "price": "20", "desc": "The full ritual"},
]

BRING_ITEMS = [
    {"num": "01", "icon": "swimwear", "label": "Swimwear",   "desc": "You'll go straight from the sauna to the sea."},
    {"num": "02", "icon": "towel",    "label": "Two towels", "desc": "One to sit on inside. One to dry off after."},
    {"num": "04", "icon": "water",    "label": "Water",      "desc": "Stay hydrated before, during, and after."},
    {"num": "05", "icon": "layer",    "label": "Warm layer", "desc": "Something cosy for after your session."},
]

BUNDLES = [
    {"name": "Loyal Bather", "sessions": 6,  "price": "100", "original": None,   "validity": "Valid 2 months", "per": "€16.67 / session"},
    {"name": "Season Pass",  "sessions": 13, "price": "200", "original": "260", "validity": "Valid 3 months", "per": "~€15 / session"},
]

GIFT_VOUCHERS = [
    {"value": "20",  "type": "Shared session"},
    {"value": "40",  "type": "Shared sessions"},
    {"value": "60",  "type": "Shared sessions"},
    {"value": "80",  "type": "Shared or Private (30 min)"},
    {"value": "100", "type": "Shared sessions"},
    {"value": "120", "type": "Private session (60 min)"},
]

PRODUCTS = [
    {"name": "Facial Oil",      "price": "25", "desc": "Naturally balanced. Post-sauna skin care.", "cat": "Skin"},
    {"name": "Tui Massage Balm","price": "15", "desc": "Sara's signature balm for muscle recovery.", "cat": "Body"},
    {"name": "Sauna + Oil",     "price": "40", "desc": "One shared session paired with a facial oil.", "cat": "Bundle", "deal": True},
    {"name": "Sauna Hat",       "price": None, "desc": "Traditional felt hat for high-heat rounds.", "cat": "Merch", "soon": True},
]

EVENTS = [
    {"title": "Sunrise Yoga & Sauna", "when": "Saturday mornings",  "desc": "Beachside yoga followed by a 45-minute sauna. Rotating guest instructors from Cork.", "tag": "Recurring"},
    {"title": "Free BBQ at the Cove", "when": "Late May 2025",      "desc": "Sara's end-of-spring celebration. Free BBQ, open sauna, live music. Everyone welcome.", "tag": "Free"},
    {"title": "Summer Wellness Days", "when": "Summer 2025",        "desc": "Sauna, guided meditation, and cold-water immersion workshops.", "tag": "Seasonal"},
]

def base_ctx():
    return {
        "nav": NAV,
        "year": datetime.now().year,
        "bookwhen": BOOKWHEN_URL,
        "revolut": REVOLUT_URL,
    }

@app.route("/")
def home():
    return render_template(
        "home.html",
        active="/",
        sessions=SESSIONS,
        bring=BRING_ITEMS,
        bundles=BUNDLES,
        vouchers=GIFT_VOUCHERS,
        **base_ctx(),
    )

@app.route("/events")
def events():
    return render_template("events.html", active="/events", events=EVENTS, **base_ctx())

@app.route("/shop")
def shop():
    return render_template("shop.html", active="/shop", products=PRODUCTS, **base_ctx())

@app.route("/about")
def about():
    return render_template("about.html", active="/about", **base_ctx())

if __name__ == "__main__":
    app.run(debug=True)
