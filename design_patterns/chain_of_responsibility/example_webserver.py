from abc import ABC, abstractmethod
from typing import Dict, Optional


class HTTPRequest:
    def __init__(self, body: Optional[Dict] = None) -> None:
        self.__body = body

    @property
    def body(self) -> Dict:
        return self.__body


class Handler(ABC):
    # Is called handler in design patterns books
    def __init__(self, next_handler=None) -> None:
        self.__next = next_handler

    @abstractmethod
    def do_handle(self, request: HTTPRequest) -> bool:
        pass

    def handle(self, request: HTTPRequest):
        result = self.do_handle(request)
        if result is False:
            # stop processing
            return

        if self.__next is not None:
            # Push process to the next step
            self.__next.handle(request)


class Authenticator(Handler):
    def do_handle(self, request: HTTPRequest) -> bool:
        # write static condition for test
        if (
            request.body.get("username") == "admin"
            and request.body.get("password") == "123"
        ):
            print("authenticate request")
            return True
        print("not authenticate request")
        return False


class Compressing(Handler):
    def do_handle(self, request: HTTPRequest) -> bool:
        print("compressing request")
        return True


class Logging(Handler):
    def do_handle(self, request: HTTPRequest) -> bool:
        print("new request was received")
        return True


class WebServer:
    def __init__(self, handler: Handler):
        self.__handler = handler

    def handle(self, request: HTTPRequest):
        self.__handler.handle(request)


if __name__ == "__main__":
    request = HTTPRequest({"username": "admin", "password": "123"})
    compressing = Compressing()
    authenticator = Authenticator(compressing)
    logging = Logging(authenticator)
    web_server = WebServer(logging)
    web_server.handle(request)

    # invalid username and password
    print("--- Test faild handler (process)")
    request = HTTPRequest({"username": "admin", "password": "1234"})
    web_server.handle(request)

    # new we can easily add new handler or remove.
    # edit handler or edit process
