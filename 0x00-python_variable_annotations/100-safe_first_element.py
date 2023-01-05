#!/usr/bin/env python3
'''augment code with correct typed annotations'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns first element of sequence if exist'''
    if lst:
        return lst[0]
    else:
        return None
