#!/usr/bin/env python3

class Dog:

    def __init__(self, name ="Mutt", breed ="Mutt"):
        self.name = name
        self.breed = breed
        print(f"A dog named {name}.")
        print(f"{name} is a {breed}.")
        

    # def bark(self):
    #     print("Woof!")

Dog("Toby", "Hound-mix")
