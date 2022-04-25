#! python3
# -*- coding: utf-8 -*-

"""__init__.py.

This file initializes the module.
"""

from flask import Flask

app = Flask(__name__)

from app import views
