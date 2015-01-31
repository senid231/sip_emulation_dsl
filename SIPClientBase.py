import sys
import os
import socket
import ssl
import time
from SIPEndpointBase import SIPEndpointBase


class SIPClientBase(SIPEndpointBase):
    """
    SIPClientBase
    """

    def __init__(self, host, port, use_ssl, auth_key, logger, pidfile):
        SIPEndpointBase.__init__(self)

        self.is_terminated = False
        self.is_disconnected = False

        self.conn = socket.socket()
        self.listener = None
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.auth_key = auth_key
        self.log = logger
        self.pidfile_path = pidfile

    def create_pidfile(self):
        pf = open(self.pidfile_path, 'w', 0)
        pf.write(str(os.getpid()))
        pf.close()

    def delete_pidfile(self):
        os.remove(self.pidfile_path)

    def sigterm_handler(self):
        self.is_terminated = True

    def set_logger(self, logger):
        self.log = logger

    def set_ssl_attrs(self, certfile, keyfile):
        pass

    def run(self):
        self.wait_for_manager()
        self.wait_for_command()

    def wait_for_manager(self):
        while self.conn is None:
            try:
                sock, address = self.listener.accept()
            except socket.error as e:
                print(e)
                time.sleep(self.config()['connection_timeout'])
                continue
            if self.use_ssl():
                sock = ssl. wrap_socket(sock, self.config()['key_file'], self.config()['cert_file'], True)
            if self.check_auth(sock, self.config()['auth_key']):
                self.__conn = sock

    def wait_for_command(self):
        pass
