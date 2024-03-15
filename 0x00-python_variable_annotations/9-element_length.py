#!/usr/bin/env python3
"""Annotation of element_length function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples of an element and its length
    """
    return [(i, len(i)) for i in lst]
