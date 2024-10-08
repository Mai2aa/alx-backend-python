#!/usr/bin/env python3
'''iterable object'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return the length of the element'''
    return [(i, len(i)) for i in lst]
