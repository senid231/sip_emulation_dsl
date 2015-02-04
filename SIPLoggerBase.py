import logging
import time

DEFAULT_FORMAT = '[%(name)s] [%(levelname)s] [%(asctime)s] %(message)s'
DEFAULT_DATE_FORMAT = '%m-%d %H:%M'
DEFAULT_LEVEL = logging.INFO


def set_simple_logger(
        name,
        filename,
        fmt=DEFAULT_FORMAT,
        date_fmt=DEFAULT_DATE_FORMAT,
        log_level=DEFAULT_LEVEL
):
    formatter = logging.Formatter(fmt=fmt, datefmt=date_fmt)
    formatter.converter = time.gmtime  # set time to GMT (UTC)
    file_handler = logging.FileHandler(filename=filename, mode='a+', encoding='UTF-8', delay=0)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    return logger
