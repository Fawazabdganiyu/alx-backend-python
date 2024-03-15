#!/usr/bin/env python3
"""Definition of make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier
    """
    def mul_func(n: float) -> float:
        """Return the result of multiplying n by multiplier
        """
        return n * multiplier
    return mul_func
