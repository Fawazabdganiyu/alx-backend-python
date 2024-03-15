#!/usr/bin/env python3
"""Definition of to_kv function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with k and the square of v
    """
    return (k, v**2)
