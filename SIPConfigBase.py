from ConfigParser import ConfigParser, NoOptionError

from ExceptionParser import ExceptionParser


class SIPConfigBase(object):
    """
    SIPConfigBase
    """
    DEFAULT_SECTION = 'DEFAULT'

    def __init__(self, file_path):
        self.__cfg = ConfigParser()
        self.__cfg.read(file_path)

    @staticmethod
    def check_section(section):
        if section is None:
            return SIPConfigBase.DEFAULT_SECTION
        else:
            return section

    def get(self, section, option):
        section = self.check_section(section)

        if self.has_option(section, option):
            return self.__cfg.get(section, option)
        else:
            return None

    def get_boolean(self, section, option):
        section = self.check_section(section)

        if self.has_option(section, option):
            return self.__cfg.getboolean(section, option)
        else:
            return None

    def get_float(self, section, option):
        section = self.check_section(section)

        if self.has_option(section, option):
            return self.__cfg.getfloat(section, option)
        else:
            return None

    def get_int(self, section, option):
        section = self.check_section(section)

        if self.has_option(section, option):
            return self.__cfg.getint(section, option)
        else:
            return None

    def get_list(self, section, option):
        section = self.check_section(section)

        if self.has_option(section, option):
            return self.__cfg.getboolean(section, option).split(',')
        else:
            return None

    def has_section(self, section):
        self.__cfg.has_section(section)

    def has_option(self, section, option):
        self.__cfg.has_option(section, option)

    def options(self, section):
        self.__cfg.options(section)

    def sections(self):
        self.__cfg.sections()
