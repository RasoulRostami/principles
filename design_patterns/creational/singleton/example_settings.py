"""
There is severl ways to implement singleton in Python.
You can see all implementations in below link.

https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Settings(metaclass=SingletonMeta):
    def __init__(self, name: str, db: str, port: int) -> None:
        self.name = name
        self.db = db
        self.port = port
        self._instance = self


if __name__ == "__main__":
    settings1 = Settings("backend", "MySQL", 80)
    print(settings1.db)

    settings2 = Settings("Front", "local", 91)
    print(settings2.db)

    print(bool(settings1 == settings2))
