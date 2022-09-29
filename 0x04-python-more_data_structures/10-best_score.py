#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    scores = list(a_dictionary.values()) 
    highscore = scores[0]
    name = ""
    for key, value in a_dictionary.items():
        if a_dictionary[key] > highscore:
            highscore = value
            name = key
    return name
