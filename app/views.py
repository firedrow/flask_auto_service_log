#! python3
# -*- coding: utf-8 -*-

"""views.py.

This file contains all the routes for Flask.
"""

from flask import render_template, request, redirect, url_for
from app import app, db


@app.route('/add', methods=['POST'])
def addLog():
    """Add logs to the database, using information from the form."""
    db.logCreate(db.db, date=request.form['date'], car=request.form['vehicle'],
                 mileage=request.form['mileage'], note=request.form['notes'])
    return redirect(url_for('index'))


@app.route('/')
def index():
    """Return the index page."""
    return render_template('index.html', logs=db.logReadAll(db.db))
