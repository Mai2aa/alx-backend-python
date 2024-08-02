#!/usr/bin/env python3
'''complex types - mixed list'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum of the list'''
    sum = 0
    for x in mxd_lst:
        sum += x
    return sum
