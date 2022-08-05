#! python3
# -*- coding: utf-8 -*-

"""views.py.

This file contains all the routes for Flask.
"""

from flask import render_template, request, redirect, url_for
from app import app, db

cars = [
    "2008 Nissan Frontier SE / 1N6AD07W98C424691",
    "2010 Chevrolet Traverse LT / 1GNLVFED3AS147696"
]


@app.route('/add', methods=['POST'])
def addLog():
    """Add logs to the database, using information from the form."""
    db.logCreate(db.db, date=request.form['date'], car=request.form['vehicle'],
                 mileage=request.form['mileage'], note=request.form['notes'])
    return redirect(url_for('index'))


@app.route('/del', methods=['GET'])
def delLog():
    """Delete log from the database."""
    milenum = request.args['milenum']
    db.logDelete(db.db, queryfield='mileage', queryterm=milenum)
    return redirect(url_for('index'))


@app.route('/')
def index():
    """Return the index page."""
    return render_template('index.html', cars=cars, logs=db.logReadAll(db.db))
