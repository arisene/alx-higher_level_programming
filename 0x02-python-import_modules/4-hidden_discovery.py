#!/usr/bin/python3
import dis, sys

def print_name(name_file):
    with open(name_file) as file:
        code = file.read
    dis.dis(code)


if __name__ == "__main__":
    print_name("hidden_4.pyc")