import configparser


class SIPConfigBase(object):
    """
    SIPConfigBase
    """

    def __init__(self, filepath):
        self.__cfg = configparser.ConfigParser()
        self.__cfg.read(filepath)

    def __getitem__(self, item):
        items = item.split(':')
        option = items[-1]
        if len(items) > 1:
            section = items[1]
        else:
            section = 'DEFAULT'

        return self.__cfg.get(section, option, fallback=None)