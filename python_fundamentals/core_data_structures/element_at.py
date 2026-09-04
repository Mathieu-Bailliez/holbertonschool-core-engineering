#!/usr/bin/env python3
"""Module: """


def element_at(my_list, idx):

    # recherche moi index 3 dans la list
    # determiner la longueur de la list
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
