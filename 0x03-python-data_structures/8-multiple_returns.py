#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None and len(sentence) > 0:
        return (len(sentence), sentence[0])
    else:
        return (len(sentence), None)
