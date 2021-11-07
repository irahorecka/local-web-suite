"""
/irahorecka/models.py
~~~~~~~~~~~~~~~~~~~~~

Module to store database models used in the Flask application.
"""

from websuite import db


class NYSE(db.Model):
    """Model stock tickers from the NYSE."""

    __tablename__ = "nyse"
    id = db.Column(db.Integer, primary_key=True)
    # General stock attributes
    name = db.Column(db.String(128))
    ticker = db.Column(db.String(8))
    live_price = db.Column(db.Float)
    day_high = db.Column(db.Float)
    day_low = db.Column(db.Float)
    # User-related attributes
    shares = db.Column(db.Integer)
    avg_cost = db.Column(db.Float)

    def __repr__(self):
        return f"NYSE(id={self.id})"
