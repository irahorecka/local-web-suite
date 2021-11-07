"""
/websuite/errors/handlers.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flask blueprint to handle errors.
"""

from flask import render_template, Blueprint

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(404)
def error_404(error):
    """Error: Page Not Found"""
    content = {
        "title": "Error 404",
    }
    return render_template("errors/404.html", content=content), 404


@errors.app_errorhandler(500)
def error_500(error):
    """Error: Internal Server Error"""
    content = {
        "title": "Error 500",
    }
    return render_template("errors/500.html", content=content), 500
