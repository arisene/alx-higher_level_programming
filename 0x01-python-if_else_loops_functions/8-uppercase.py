#!/usr/bin/python3
def uppercase(str):
    uppercase_text = ""
    for wd in str:
        if "a" <= wd <= "z":
            uppercase_char = chr(ord(wd) - 32)
            uppercase_text += uppercase_char
        else:
            uppercase_text += wd
    return(print("{}".format(uppercase_text)))