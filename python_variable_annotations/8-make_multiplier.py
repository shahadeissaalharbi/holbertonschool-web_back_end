#!/usr/bin/env python3
"""Module that provides a type-annotated multiplier-function factory."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_function(value: float) -> float:
        """Multiply the given value by the enclosing multiplier."""
        return value * multiplier
    return multiplier_function
