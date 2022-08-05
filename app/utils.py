#! python3
# -*- coding: utf-8 -*-

"""utils.py.

This file contains some utility functions for Flask.
"""
from app import app


@app.template_filter()
def splitpart(value, index, char=','):
    """Split string function for Jinja."""
    return value.split(char)[index]
