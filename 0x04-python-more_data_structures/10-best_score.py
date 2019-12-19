#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    i = []
    for new in a_dictionary:
        i.append(new)
    return max(i)
