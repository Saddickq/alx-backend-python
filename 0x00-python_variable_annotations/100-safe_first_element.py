#!/usr/bin/env python3
""" Module documentation """
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Main method"""
    if lst:
        return lst[0]
    else:
        return None
