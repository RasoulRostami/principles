"""
Description
it is usefull when we have got piplines or chain of objects call after each other

Example:
Webserver get a http request and do something in a piplien, for example authenticate, logging, compression and etc.
"""


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

    def handler(self, request):
        self.authenticator.authenticate(request)
        self.logger.logging(request)
        self.compressor.compress(request)


class HttpRequest:
    pass


print("=========== Without chain of responsibility")
request = HttpRequest()
web_server = WebServer()
web_server.handler(request)

# problem
# This implement is not as good enught.
# it is vailot open/close principal and single responsiblity
# when we want to add/change/remove/change ordering of pipline
# we need to modify WebServer class
#
# Best way to handle pipline like this is using chain of responsibility and template method toghether
# In chain of responsibility if one step is faild, pipline break and next pipline will not run
# in chain of responsibiltiy each step shoud know his next one
#
import abc


class Process(abc.ABC):
    def __init__(self, next_one=None) -> None:
        self.next_one = next_one

    @abc.abstractmethod
    def do_handle(self, request) -> bool:
        pass

    def handle(self, request):
        result = self.do_handle(request)
        if result is False:
            return
        if self.next_one is not None:
            self.next_one.handle(request)


class AuthenticatorV1(Process):
    def do_handle(self, request) -> bool:
        print("authenticate")
        return True


class LoggerV1(Process):
    def do_handle(self, request) -> bool:
        print("logging")
        return True


class CompressorV1(Process):
    def do_handle(self, request) -> bool:
        print("compress")
        return True


class FaildProcess(Process):
    def do_handle(self, request) -> bool:
        print("faild")
        return False


class WevServerV1:
    def __init__(self, handler) -> None:
        self.handler = handler

    def handle(self, request):
        self.handler.handle(request)


# Using
# define process and pipline reverse
print("=========== With chain of responsibility")
compress = CompressorV1()
logger = LoggerV1(compress)
auth = AuthenticatorV1(logger)
server = WevServerV1(auth)
server.handle(request)
# now we can change piplines very easily
print("=========== failed pipeline")
compress1 = CompressorV1()
faildprocess = FaildProcess(compress)
server = WevServerV1(faildprocess)
server.handle(request)
