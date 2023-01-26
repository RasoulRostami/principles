"""
Description:
Encapsulation is a way to restrict the direct access to some components of an object

Example:
You have written a bank application. there is a Account class with balance attribute.
As you know balance can not be negative number, but if you let other developer to change it
what will happen. they might write invalid data. How we can protect our information.
protect our information and direct access is called encapsulation.
"""


class Client:
    def __init__(self, name) -> None:
        self.name = name
        self.__age = 0

    @property
    def age(self) -> str:
        print(f"getter method called for {self.name}")
        return "{} is {} years old!".format(self.name, self.__age)

    @age.setter
    def age(self, age: int):
        print(f"setter method called for {self.name}")
        if age < 0:
            raise ValueError("Age can not be negative!")
        self.__age = age


# Encapsulation is not mean use setter and getter
# We can implement them with actions
class Account:
    def __init__(self) -> None:
        self.__balance = 0

    def withdrawal(self, amount: int):
        if not (amount > 0 and self.__balance - amount > 0):
            raise ValueError("HAHA: you can not withdrawal {}".format(amount))
        self.__balance -= amount
        print(f"withdrawal {amount} successfully")

    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError("HAHA: you can not deposit {}".format(amount))
        self.__balance += amount
        print(f"deposit {amount} successfully")

    def info(self):
        print("Balance is  {}".format(self.__balance))


if __name__ == "__main__":
    tom = Client("Tom")
    john = Client("John")

    print("--------- Use setter and getter -------------------")
    tom.age = 20
    print(tom.age)

    print("-------- Test setter ------------------------------")
    try:
        john.age = -2
    except ValueError:
        print("HAHA: you can not negative age for clients")

    print("------ Access to private data directly ------------")
    account = Account()
    try:
        print(account.__balance)
    except:
        print("HAHA: you can not access private data directly")

    print("---------- implement modern encapsulation- ---------")
    try:
        account.deposit(-20)
    except Exception as e:
        print(str(e))

    account.deposit(20)

    try:
        account.withdrawal(40)
    except Exception as e:
        print(str(e))

    account.withdrawal(10)
    account.info()
