"""
TinyDB Base functions.

This file contains a set of baseline functions to interact with TinyDB database
to be used with a Flask front-end in the future.
"""

import json
from tinydb import TinyDB, Query

db = TinyDB('app/db/service_log.db')


def logCreate(db: TinyDB, date: str = None, car: str = None,
              mileage: int = None, note: str = None):
    """Create new record in the database."""
    db.insert({'date': date,
               'vehicle': car,
               'mileage': mileage,
               'note': note})


def logReadAll(db: TinyDB):
    """Read all entries in the database."""
    return list(db)


def logUpdate(db: TinyDB, queryfield: str = None,
              queryterm: str | int = None, change: json = None):
    """Update a record in the database, based on the query."""
    db.update(change, Query()[queryfield] == queryterm)


def logDelete(db: TinyDB, queryfield: str = None,
              queryterm: str | int = None):
    """Delete a record in the database, based on the query."""
    db.remove(Query()[queryfield] == queryterm)


"""
db.truncate()  # clear database before testing
logCreate(db, car='2010 Nissan Frontier', mileage=123456,
          note='Oil Change - 5.5qt 5W30, K&N HP-1010 filter')
logCreate(db, car='2010 Nissan Frontier', mileage=128456,
          note='Oil Change - 5.5qt 5W30, K&N HP-1010 filter')
logCreate(db, car='2010 Nissan Frontier', mileage=133456,
          note='Oil Change - 5.5qt 5W30, K&N HP-1010 filter')
logReadAll(db)
logUpdate(db, queryfield='mileage', queryterm=123456,
          change={'mileage': 124567})
logReadAll(db)
logDelete(db, queryfield='mileage', queryterm=124567)
logReadAll(db)
"""
