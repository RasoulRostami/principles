# We are going to develop send message system
class Message:
    def __init__(self, message: str) -> None:
        self.message = message


class Connect:
    def disconnect(self):
        print("disconnect")


class Authenticate:
    def authenticate(self, username, password):
        return "token"


class PushMessage:
    def send(self, token, message, target):
        print(f"new message to {target}")


if __name__ == "__main__":
    # send message
    message = Message("Hello!")
    connect = Connect()
    token = Authenticate().authenticate("user", "pass")
    PushMessage().send(token, message, "user")
    connect.disconnect()
    # we need to use above code when we send a new push message
    # There are tow main problem
    # 1. Using above code is hard, This is crowd
    # 2. There are many coupling and if one of this methods changes we need to modify
    #    many files.
    # In that case we use facade patterns
