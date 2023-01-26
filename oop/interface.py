###########
# Coupling
###########
"""
How much a class or a module depends on another classes or modules
Example:
"""


class Tax2021:
    def tax(self):
        return 0.1


class Tax2022:
    def tax(self):
        return 0.2


class Salary:
    def __init__(self, salary: int) -> None:
        self.salary = salary

    def get_tax(self):
        return f"Tax is {Tax2021().tax()}"

    def include_tax(self):
        tax = Tax2021()
        return "Salary include tax is {}".format(self.salary + self.salary * tax.tax())


salary = Salary(10)
print("--------- Normal example ---------")
print(salary.get_tax())
print(salary.include_tax())
# Problem
"""
As you can see, we use Tax2021 class in the Salary class,
What happens if we use Tax2022 instead of Tax2021
what happens if Tax2022 needs to have some methods more than Tax2021
What happens if Tax2022 hasn't tax method
"""

# Solutions
"""
Interface can help us decrease coupling and have reliable codes
Like classes, interfaces define methods.
Unlike classes, these methods are abstract.
An abstract method is one that the interface simply defines
We can not instantiate interface classes

Note: Python has not interface like Java, Interface is not necessary in python
      we can mention interface by ABC and python-interface package
Note: In Java Interface class can not instantiate or have non abstract method
"""

# Example
import abc


class InterfaceUser(abc.ABC):
    @abc.abstractclassmethod
    def speak(self):
        pass


class Student(InterfaceUser):
    pass


class Teacher:
    def speak(self):
        print("Teacher is speaking")


class Manager:
    def speak(self):
        print("manager is speaking")


print("--------- Interface example -----------")
try:
    user = InterfaceUser()
except TypeError:
    print("HAHA: We can not instantiate class that have abstract method")
    print("Note: If you don't inherit from ABC, you can instantiate Animal class")

try:
    student = Student()
except TypeError:
    print("HAHA: Student has not implemented speak method")

teacher = Teacher()
teacher.speak()

print("--------- Decrease coupling --------")
# Now, we no all people can speak, No matter he is teacher, student or manager
# And everyone has their own behavior
class Meating:
    def present(self):
        user1 = self.get_manager()
        user2 = self.get_teacher()
        user1.speak()
        user2.speak()

    def get_manager(self) -> InterfaceUser:
        return Manager()

    def get_teacher(self) -> InterfaceUser:
        return Teacher()


Meating().present()
