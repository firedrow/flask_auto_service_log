#! python3
# -*- coding: utf-8 -*-

"""views.py.

This file contains all the routes for Flask.
"""

from flask import render_template, redirect, url_for
from app import app, db


@app.route('/')
def index():
    """Return the index page."""
    return render_template('index.html', logs=db.logReadAll(db.db))