#!/usr/bin/env python3
'''Complex types'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns the sum as a float'''
    sum = 0
    for x in input_list:
        sum += x
    return sum
