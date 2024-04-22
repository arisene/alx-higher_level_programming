#/usr/bin/python3

def lookup(obj):
    list_methods = list()
    list_methods.append(dir(obj))

    return list_methods[0]