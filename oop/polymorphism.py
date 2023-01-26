"""
Description:
polymorphous means 'many forms'.
Take ability to object act many forms.
each class can have different behavior

Story:
Imagine all animals can walk, but Does all animals walk same? No.
Some of them are fast, some of them are slow, some of them flying and
some of them swimming. But All of them can walk.

Example:
We would like to implement zoo application. Shall we implement walk action for
all of them. No we can have an abstraction class and each class can have own behavior
"""


class Animal:
    def escape(self):
        print("walk very fast")

    def walk(self):
        print("Normal walk")


class Cat(Animal):
    pass


class Tiger(Animal):
    def walk(self):
        print("tiger walk very fast")


class Turtle(Animal):
    def walk(self):
        print("turtle walk slowly")


if __name__ == "__main__":
    cat = Cat()
    tiger = Tiger()
    turtle = Turtle()

    cat.walk()
    tiger.walk()
    turtle.walk()
