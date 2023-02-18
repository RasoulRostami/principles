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


class SendMessageService:
    def send(self, message: str, target: str):
        connect = Connect()
        token = Authenticate().authenticate("user", "pass")
        PushMessage().send(token, Message(message), "user")
        connect.disconnect()


if __name__ == "__main__":
    # send message
    service = SendMessageService()
    service.send("Hello", "Iser")
    # Now we use only one service in our codes and if one of this code
    # has beed changed we only need modify one file.
