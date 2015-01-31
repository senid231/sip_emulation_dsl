import sys
import struct
import pickle
import socket


class SIPSocketWrapper(object):
    """
    title
    """
    PACK_INT_FMT = '!I'

    def __init__(self, sock):
        self.__sock = sock

    def send(self, msg):
        data = pickle.dumps(msg)
        size = bytes(struct.pack(self.PACK_INT_FMT, len(data)))
        self.__sock.sendall(size)
        self.__sock.sendall(data)

    def receive(self):
        size = struct.unpack(self.PACK_INT_FMT, self.__raw_receive(4))[0]
        data = self.__raw_receive(size)
        return pickle.loads(data)

    def __raw_receive(self, size):
        if size <= 0:
            return

        count = 0
        data = ''
        while count != size:
            temp = self.__sock.recv(size - count)
            count += len(temp)
            data += temp

        return data
