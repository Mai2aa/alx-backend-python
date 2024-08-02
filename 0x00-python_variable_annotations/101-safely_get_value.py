#!/usr/bin/env python3
'''more involved type annotations'''
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
d_var = Union[T, None]
r_var = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: d_var = None) -> r_var:
    '''returns a value in  a dict'''
    if key in dct:
        return dct[key]
    else:
        return default
