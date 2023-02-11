# Todo application
#
# We would like to log all activities

import abc


class ActivityLogger:
    def logging(self, msg=""):
        print("> Activity log", msg)


class Task(abc.ABC):
    # Called 'abstrac class' in books
    def __init__(self) -> None:
        self.logger = ActivityLogger()

    def logging(self):
        self.logger.logging()

    def execute(self):
        self._do_execute()
        self.logging()

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


class RemoveTask(Task):
    def _do_execute(self):
        print("remove a task")

    def logging(self):
        self.logger.logging("remove a task")


# Protected method
# protected method can be used in main class and its sub classes (children)
# public method can use in classes, sub classes and instances
# In this example we need sub classes use do_execute but instances can't call this method,
# so we used protected method
# private method only can use in main class

if __name__ == "__main__":
    create_task = CreateTask()
    update_task = UpdateTask()
    remove_task = RemoveTask()

    create_task.execute()
    update_task.execute()
    remove_task.execute()
