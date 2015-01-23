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

    @staticmethod
    def check_section(section):
        if section is None:
            return 'default'
        else:
            return section

    def get(self, section, option):
        section = self.check_section(section)
        return self.__cfg.get(section, option, fallback=None)

    def get_boolean(self, section, option):
        section = self.check_section(section)
        return self.__cfg.getboolean(section, option, fallback=None)

    def get_float(self, section, option):
        section = self.check_section(section)
        return self.__cfg.getfloat(section, option, fallback=None)

    def get_int(self, section, option):
        section = self.check_section(section)
        return self.__cfg.getint(section, option, fallback=None)

    def get_list(self, section, option):
        section = self.check_section(section)
        return self.__cfg.get(section, option, fallback='').split(',')
