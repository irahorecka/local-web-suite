"""
/websuite/main/routes.py
~~~~~~~~~~~~~~~~~~~~~~~~

Flask blueprint to handle routes for local.
"""

from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Landing page of websuite."""
    content = {
        "title": "Home | WebSuite",
    }
    return render_template("main/index.html", content=content)


@main.route("/settings")
def settings():
    """Settings page of websuite."""
    content = {
        "title": "Settings | WebSuite",
    }
    return render_template("main/settings.html", content=content)
