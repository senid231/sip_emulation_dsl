import sys
import struct
import pickle
import socket

from ExceptionParser import ExceptionParser


class SIPSocketWrapper(object):
    """
    simple socket wrapper
    """
    PACK_INT_FMT = '!I'

    def __init__(self, sock):
        self.__sock = sock
        self.is_broken = False

    def send(self, msg):
        data = pickle.dumps(msg)
        data_length = len(data)
        size = bytes(struct.pack(self.PACK_INT_FMT, data_length))

        try:
            self.__sock.sendall(size)
            self.__sock.sendall(data)
        except socket.error:
            self.log(ExceptionParser().printable())
            self.is_broken = True
            return None

        return data_length

    def receive(self):
        size = struct.unpack(self.PACK_INT_FMT, self.__raw_receive(4))[0]
        data = self.__raw_receive(size)

        if data is None:
            return None

        return pickle.loads(data)

    def __raw_receive(self, size):
        if size is None or size <= 0:
            return None

        count = 0
        data = ''

        while count != size:
            temp = self.__sock.recv(size - count)
            if temp == '':
                self.is_broken = False
                return None
            count += len(temp)
            data += temp

        return data

    @staticmethod
    def log(msg):
        print(msg)