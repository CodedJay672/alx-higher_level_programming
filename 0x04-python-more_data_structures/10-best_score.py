#!/usr/bin/python3
def best_score(a_dictionary):
    highscore = 0
    name = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for key, value in a_dictionary.items():
        if a_dictionary[key] > highscore:
            highscore = value
            name = key
    return name
