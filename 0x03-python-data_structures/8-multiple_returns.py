#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        res = (len(sentence), sentence[0])
        return res
    else:
        res = (len(sentence), None)
        return res
