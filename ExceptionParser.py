import linecache
import sys


class ExceptionParser(object):
    """
    simple exception parser

    type - exception class
    filename - name of file that raise exception
    line - line of that file that raise exception
    line_number - line number of that line
    value - exception message
    """

    def __init__(self):
        self.type, self.value, self.traceback = sys.exc_info()
        self.traceback_frame = self.traceback.tb_frame
        self.line_number = self.traceback.tb_lineno
        self.filename = self.traceback_frame.f_code.co_filename
        linecache.checkcache(self.filename)
        self.line = linecache.getline(self.filename, self.line_number, self.traceback_frame.f_globals).strip()

    def print_attributes(self):
        print('Type: %s' % self.type)
        print('Filename: %s' % self.filename)
        print('Line number: %s' % self.line_number)
        print('Line: %s' % self.line)
        print('Value %s' % self.value)

    def printable(self):
        return "Error <%s>: %s\n%s:%s\n%s" % (self.type, self.value, self.filename, self.line_number, self.line)
