from abc import ABC, abstractclassmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already Open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is alrady Closed")
        self.opened = False

    @abstractclassmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from the network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from Memory stream")


stream = MemoryStream()
stream.open()
