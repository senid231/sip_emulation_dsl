import socket
from SIPEndpointBase import SIPEndpointBase


class SIPManagerBase(SIPEndpointBase):
    """
    SIPManagerBase
    """

    def __init__(self):
        pass

    def start(self):
        for client_address in self.__clients_addresses:
            self.connect_to_client(client_address)

        for test in self.tests():
            eval(test).run(self.clients, self.config())
