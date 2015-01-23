from ConfigParser import ConfigParser, NoOptionError


class SIPConfigBase(object):
    """
    SIPConfigBase
    """
    DEFAULT_SECTION = 'DEAFULT'

    def __init__(self, filepath):
        self.__cfg = ConfigParser()
        self.__cfg.read(filepath)

    def __getitem__(self, item):
        items = item.split(':')
        option = items[-1]
        if len(items) > 1:
            section = items[1]
        else:
            section = self.DEFAULT_SECTION

        return self.__cfg.get(section, option, fallback=None)

    @staticmethod
    def check_section(section):
        if section is None:
            return SIPConfigBase.DEFAULT_SECTION
        else:
            return section

    def get(self, section, option):
        section = self.check_section(section)
        ret = None
        try:
            ret = self.__cfg.get(section, option)
        except NoOptionError as e:
            print(e)
        return ret

    def get_boolean(self, section, option):
        section = self.check_section(section)
        ret = None
        try:
            ret = self.__cfg.getboolean(section, option)
        except NoOptionError as e:
            print(e)
        return ret

    def get_float(self, section, option):
        section = self.check_section(section)
        ret = None
        try:
            ret = self.__cfg.getfloat(section, option)
        except NoOptionError as e:
            print(e)
        return ret

    def get_int(self, section, option):
        section = self.check_section(section)
        ret = None
        try:
            ret = self.__cfg.getint(section, option)
        except NoOptionError as e:
            print(e)
        return ret

    def get_list(self, section, option):
        section = self.check_section(section)
        ret = []
        try:
            ret = self.__cfg.get(section, option).split(',')
        except NoOptionError as e:
            print(e)
        return ret
