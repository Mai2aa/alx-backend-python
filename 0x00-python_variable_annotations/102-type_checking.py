#!/usr/bin/env python3
'''Type checking'''
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' zoom array function'''
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x: List[int] = zoom_array(tuple(array))

zoom_3x: List[int] = zoom_array(tuple(array), 3)
