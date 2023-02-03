"""
Description:
Use template method when we have commen code, or we need to face somethong for instances.

Problem:
Imagine we want to design bank application, Clients have got some activities and we need to log all their activity;
look the first design and then I will describe more about problems.
"""


class ActivityLog:
    def log(self):
        print("logging activity")


class Deposit:
    def __init__(self) -> None:
        self.activity_log = ActivityLog()

    def deposit(self):
        print("client deposit from his/her account.")
        self.activity_log.log()


class Withdraw:
    def __init__(self) -> None:
        self.activity_log = ActivityLog()

    def withdraw(self):
        print("client withdraw from her account.")
        self.activity_log.log()


print("============ Normal codes ============")
deposit = Deposit()
withdraw = Withdraw()
deposit.deposit()
withdraw.withdraw()

# Problems:
# 1. we will have to many duplicate codes
# 2. we might forget to use activity log
# 3. we are not forced to implement log function to our method or class,
# when a new developer join to team, he will violate rules.
# we now we will use template method factory to solve problems and implement a task manager.

import abc


class Task(abc.ABC):
    def __init__(self) -> None:
        self.activity_log = ActivityLog()

    def execute(self):
        self._do_execute()
        self.activity_log.log()

    @abc.abstractmethod
    def _do_execute(self):
        # this is a protected method.
        pass


class CreateTask(Task):
    def _do_execute(self):
        print("create a task")


class UpdateTask(Task):
    def _do_execute(self):
        print("update a task")


# Protected method
# protected method can use in main class and its sub classes (children)
# public method can use in classes, sub classes and instances
# In this example we need sub classes use do_execute but instances can't call this method,
# so we used protected method
# private method only can use in main class

print("====================== Use Template mthod Design pattern")
create_task = CreateTask()
update_task = UpdateTask()

create_task.execute()
update_task.execute()
