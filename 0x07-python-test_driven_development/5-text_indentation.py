#!/usr/bin/python3
"""
Module 5 print text
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for line in text:
        print(line, end="")
        for eleh in line:
            if eleh =='.' or eleh == '?'or eleh == ':':
                print("\n")
                

    print()