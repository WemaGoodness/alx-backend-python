#!/usr/bin/env python3
from typing import Mapping, TypeVar, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Retrieves the value for a given key from a dictionary if it exists.
    Returns the default value if the key is not present.
    Parameters:
    dct (Mapping[Any, T]): A mapping (dictionary) where the keys can be of any type
                            and the values are of type T.
    key (Any): The key to look up in the dictionary.
    default (Union[T, None]): The default value to return if the key is not found.
    Returns:
    Union[T, None]: The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
