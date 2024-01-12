#!/usr/bin/env python3
""" Module documentation """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Main method """
    return [(i, len(i)) for i in lst]
