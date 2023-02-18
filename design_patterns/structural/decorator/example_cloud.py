# we are going to develop could stream service
# ---------- Fist: How to implement purly
from abc import ABC, abstractmethod


class Stream:
    def write(self, data):
        pass


class CloudStream(Stream):
    def write(self, data):
        print(f"writing {data}")


class CompressCloudStream(Stream):
    def __init__(self, stream: Stream) -> None:
        self.stream = stream

    def write(self, data):
        data = data[:5]
        self.stream.write(data)


class EncryptCloudStream(CloudStream):
    def __init__(self, stream: Stream) -> None:
        self.stream = stream

    def write(self, data):
        data = "wrwe32423cs"
        self.stream.write(data)


# ---------- Second: How to implement in python
def compress(fun):
    def wrapper(self, data):
        if len(data) > 10:
            data = data[:5]
        fun(self, data)

    return wrapper


def encrypt(fun):
    def wrapper(self, data: str):
        if data.isdigit():
            data = data[::-1]
        fun(self, data)

    return wrapper


class Database:
    @compress
    @encrypt
    def write(self, data):
        print(f"writing {data}")


if __name__ == "__main__":
    cloud_stream = CloudStream()
    cloud_stream.write("Photos")

    compress = CompressCloudStream(CloudStream())
    compress.write("I am john smit")

    encrypt = EncryptCloudStream(CloudStream())
    encrypt.write("Account")

    encrypt_and_compress = EncryptCloudStream(CompressCloudStream(CloudStream()))
    encrypt_and_compress.write("how are you")

    print("----- database -----")
    db = Database()
    db.write("hello!")
    db.write("12345678901234")
