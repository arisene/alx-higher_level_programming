#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    max_key = None
    for k, y in a_dictionary.items():
        if max_key is None or max_score < y:
            max_score = y
            max_key = k

    return max_key
