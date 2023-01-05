#!/usr/bin/env python3
'''add type annotations to function'''

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Returns value from a dict using a given parameter key'''
    if key in dct:
        return dct[key]
    else:
        return default
