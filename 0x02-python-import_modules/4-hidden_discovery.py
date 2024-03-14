#!/usr/bin/python3
import dis


def print_defined_names(filename):

    with open(filename, 'rb') as file:
        code = file.read()

    # Disassemble the bytecode
    instructions = dis.get_instructions(code)

    # Extract and print names
    names = set()
    for instr in instructions:
        if instr.opname == 'LOAD_NAME' and not instr.argval.startswith('__'):
            names.add(instr.argval)

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    print_defined_names("hidden_4.pyc")
