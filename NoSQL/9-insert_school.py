#!/usr/bin/env python3
"""Module that provides a function to insert a document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: fields and values for the new document.

    Returns:
        The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
