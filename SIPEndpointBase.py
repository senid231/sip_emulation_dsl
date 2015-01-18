class SIPEndpointBase(object):
    """SIPEndpointBase"""

    def __init__(self):
        self.__config = None
        self.__host = ""
        self.__port = 9999

        self.__use_ssl = False
        self.__log = None

    def config(self, arg=None):
        if arg is not None:
            self.__config = arg
        else:
            return self.__config

    def host(self, arg=None):
        if arg is not None:
            self.__host = arg
        else:
            return self.__host

    def port(self, arg=None):
        if arg is not None:
            self.__port = arg
        else:
            return self.__port

    def use_ssl(self, arg=None):
        if arg is not None:
            self.__use_ssl = arg
        else:
            return self.__use_ssl

    def logger(self, arg=None):
        if arg is not None:
            self.__log = arg
        else:
            return self.__log
