#!/usr/bin/env python3

from difflib import SequenceMatcher


def search_similar_str(text, substr):
    leader = (0, set())

    for window in (text[i:i + len(substr)] for i in range(len(text) - len(substr) + 1)):
        seq = SequenceMatcher(a=window, b=substr)
        score = seq.ratio()
        if score > leader[0]:
            leader = (score, {window})
        elif score == leader[0]:
            leader[1].add(window)
        if leader[0] == 1:
            return leader
        print(score, window, substr)

    return leader


if __name__ == '__main__':
    a = "ACATCTATGGACATTACCCC"
    b = "CTATGAGC"
    print('Searched:', search_similar_str(a, b))
