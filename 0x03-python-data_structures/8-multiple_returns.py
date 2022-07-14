#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        for a in range(len(sentence)):
            length = len(sentence)
            first = sentence[0]
            out = length, first
            return(out)
    else:
        length = len(sentence)
        first = None
        out = length, first
        return(out)
