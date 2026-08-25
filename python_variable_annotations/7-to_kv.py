#!/usr/bin/env python3
"""Module that provides a type-annotated key-value tuple function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the given key and the square of the given value."""
    return (k, float(v ** 2))
