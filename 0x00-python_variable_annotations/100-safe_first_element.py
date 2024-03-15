#!/usr/bin/env python3
"""Annotation of safe_first_element function
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of lst if exists, else None
    """
    if lst:
        return lst[0]
    else:
        return None
