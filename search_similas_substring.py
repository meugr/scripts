#!/usr/bin/env python

from difflib import SequenceMatcher


def get_subs(seq, length):
    """Generates all substrings of a given length"""
    for i in range(len(seq) - length + 1):
        yield seq[i: i + length]


a = "ACATCTATGGACATTACCCC"
b = "CTATGAGC"
leader = [0, '']

for window in get_subs(a, len(b)):
    seq = SequenceMatcher(a=window, b=b)
    score = seq.ratio()
    if score > leader[0]:
        leader = [score, [window]]
    elif score == leader[0]:
        leader[1].append(window)
    print(score, window, b)
print('======')
print(leader)

