"""
We are developing an application and there is a settings class,
We need to create settings instance once and use it everywhere.

"""


class Settings:
    def __init__(self, name: str, db: str, port: int) -> None:
        self.name = name
        self.db = db
        self.port = port


if __name__ == "__main__":
    settings1 = Settings("backend", "MySQL", 80)
    print(settings1.db)

    settings2 = Settings("Front", "local", 91)
    print(settings2.db)

    print(bool(settings1 == settings2))

# Problem
# As you see the above code is not working and return invalid value.
# In this code we can change settings values easily and we have not same
# settings during our application.
