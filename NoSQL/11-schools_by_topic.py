#!/usr/bin/env python3
"""Module that provides a function to find schools by topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): the topic searched.

    Returns:
        A list of matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
