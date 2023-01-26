"""
Description:
When a class derives from another class

Example:
In an offce we have many roles. Manager, Assistence, Staff, Developer, Secretriy and so on.
What are you doing when you want to develop office application,
Do you create a class per role, What are you doing with dublicate data and action? Do you copy them?
What if one action is change? Do you modify all classes.

with interitace we can solve above problems. we write duplicate code in one class and others use them
"""


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def ask(self):
        print(f"{self.name} asks")

    def listen(self):
        print(f"{self.name} listens")

    def work(self):
        print(f"{self.name} works")


class Manager(Person):
    pass


class Developer(Person):
    pass


class Staff(Person):
    pass


if __name__ == "__main__":
    tom = Manager("Tom")
    jessi = Developer("Jessi")
    inna = Staff("Inna")

    tom.ask()
    jessi.listen()
    inna.work()
