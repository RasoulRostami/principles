"""
Description:
Abstraction means, reduce complexity by hiding unnecessary data

Story:
When you using remote control, to change channels and work with TV, you don't know
how exactly it work, you don't know about connections, modem and electric boards. only
push the buttons.

Example:
In programming you can hiding extra actions and use class easily
like below. when you want to send an email, many thing happens
but other developers don't know what happens, they only use send method
"""


class SendMail:
    def __connect(self):
        print("Connect to email server")

    def __disconnect(self):
        print("Disconnect from server")

    def __validate_information(self):
        print("Validate information")

    def send(self, content: str) -> None:
        self.__validate_information()
        self.__connect()
        print("send {} email".format(content))
        self.__disconnect()


if __name__ == "__main__":
    send_mail = SendMail()
    send_mail.send("HELLO")
