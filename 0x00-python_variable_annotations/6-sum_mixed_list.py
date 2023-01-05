#!/usr/bin/env python3
'''type-annotated function sum_mixed_list'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''returns sum of mxd_list as a float'''
    return float(sum(mxd_list))
