# Design a webserver application, get HTTP request and handle it
from typing import Dict, Optional


class HTTPRequest:
    def __init__(self, body: Optional[Dict] = None) -> None:
        self.__body = body

    @property
    def body(self) -> Dict:
        return self.__body


class Authenticator:
    def authenticate(self, request):
        print("Authenticate")


class Logger:
    def logging(self, request):
        print("logging")


class Compressor:
    def compress(self, request):
        print("compressing")


class WebServer:
    def __init__(self) -> None:
        self.authenticator = Authenticator()
        self.logger = Logger()
        self.compressor = Compressor()

    def handler(self, request: HTTPRequest):
        self.authenticator.authenticate(request)
        self.logger.logging(request)
        self.compressor.compress(request)


if __name__ == "__main__":
    request = HTTPRequest()
    web_server = WebServer()
    web_server.handler(request)

# It work but is is not good design.
# When we want to change ordering, add/remove handler, update conditions and behavior
# we Will need to modify codes.
# WebServer class violate single responsibility principal.
