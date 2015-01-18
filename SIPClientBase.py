import socket
import ssl
import time
from SIPEndpointBase import SIPEndpointBase


class SIPClientBase(SIPEndpointBase):
    """
    SIPClientBase
    """

    def __init__(self):
        SIPEndpointBase.__init__()
        self.__listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__conn = None

    def conn(self):
        self.__conn

    def start(self):
        self.wait_for_manager()
        self.wait_for_command()

    def wait_for_manager(self):
        while self.__conn is None:
            try:
                sock, address = self.__listener.accept()
            except ConnectionError as e:
                print(e)
                time.sleep(self.config()['connection_timeout'])
                continue
            if self.use_ssl():
                sock = ssl. wrap_socket(sock, self.config()['key_file'], self.config()['cert_file'], True)
            if self.check_auth(sock, self.config()['auth_key']):
                self.__conn = sock

    def wait_for_command(self):
        pass