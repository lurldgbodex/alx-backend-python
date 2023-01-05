#!/usr/bin/env python3
'''type-annotated function sum_list'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns sum of input list args'''
    sum_of_value: float = 0
    for values in input_list:
        sum_of_value += values
    return sum_of_value
