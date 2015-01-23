from ConfigParser import ConfigParser


class SIPConfigBase(object):
    """
    SIPConfigBase
    """

    def __init__(self, filepath):
        self.__cfg = ConfigParser()
        self.__cfg.read(filepath)

    def __getitem__(self, item):
        items = item.split(':')
        option = items[-1]
        if len(items) > 1:
            section = items[1]
        else:
            section = 'DEFAULT'

        return self.__cfg.get(section, option, fallback=None)

    def get(self, section, option):
        if section is None:
            section = 'default'

        value = self.__cfg.get(section, option, fallback=None)

        if value in ['True', 'true']:
            value = True
        elif value in ['False', 'false']:
            value = False

        return value