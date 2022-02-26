from collections import defaultdict
import math
from typing import Any


def __build_dictionary_with_grouped_numbers(ar: list) -> dict[Any, list]:
    keys = defaultdict(list)
    for key, value in enumerate(ar):
        keys[value].append(key)
    return keys


def __validate_quantities_of_numbers_that_have_pars(
        keys: dict[Any, list]) -> int:
    quantity_par = 0
    for value in keys:
        if len(keys[value]) > 1:
            quantity_par += math.floor(len(keys[value]) / 2)
    return quantity_par


def __number_of_pairs(ar: list) -> int:
    keys = __build_dictionary_with_grouped_numbers(ar)
    quantity_par = __validate_quantities_of_numbers_that_have_pars(keys)
    return quantity_par


def sock_merchant(ar: list) -> int:
    return __number_of_pairs(ar)
