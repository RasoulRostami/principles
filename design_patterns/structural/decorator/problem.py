# We are developing CloudStream service
class CloudStream:
    def write(self, data):
        print(f"writing {data}")


# After a few while your manager ask you to compress data in they are big
class CompressCloudStream(CloudStream):
    def write(self, data):
        print(f"writing {data[:5]}")


# After a few while your manager ask you to encrypted data befre writing
class EncryptCloudStream(CloudStream):
    def write(self, data):
        data = "wrwe32423cs"
        print(f"writing {data}")


# After a few while your manager ask you to encrypted data befre writing
class EncryptAndCompressCloudStream(CloudStream):
    def write(self, data):
        data = data[:5]
        data = "qxwxxf"
        print(f"writing {data}")


# After a few while your manager ask you ...
# Oh, command how many subclass would you like to create
# you can not create new subclass for each requirment
# you can not dublicate codes
# you can not chain the classes

if __name__ == "__main__":
    cloud_stream = CloudStream()
    cloud_stream.write("Photos")

    compress = CompressCloudStream()
    compress.write("I am john smit")

    encrypt = EncryptCloudStream()
    encrypt.write("Account")

    encrypt_and_compress = EncryptAndCompressCloudStream()
    encrypt_and_compress.write("how are you")
