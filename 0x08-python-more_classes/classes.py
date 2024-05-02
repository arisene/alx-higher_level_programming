#!/usr/bin/python3
class Solomon:

    def __init__(self):
        self.name = "Salomon"
        self.age = 50
    def get_name(self):
        print(f"Hello, my name is {self.name}")
    def get_age(self):
        print(f"I am {self.age}")
persone1 = Solomon()
persone2 = Charles()

for person in (persone1, persone2):
    person.get_name()
    person.get_age()