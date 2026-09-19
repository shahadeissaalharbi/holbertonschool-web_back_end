#!/usr/bin/env python3
"""Module that provides a function to list all documents in a collection."""


def list_all(mongo_collection):
    """List all documents in a collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents, or an empty list if none exist.
    """
    return list(mongo_collection.find())
