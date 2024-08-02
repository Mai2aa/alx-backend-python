#!/usr/bin/env python3
'''complex types - functions'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier'''
    return lambda x: x * multiplier
