"""
The logconfig.py module offers a default configuration and convenience functions
and can be dropped directly into any python application.
This is essentially a template which can be copied into a python project and
used to easily achieve a good practice of logging.
Usage: call `setup_logging` only once from the application main() function or __main__ module.
"""
import logging.config
import sys
from colorama import Fore, init, Back
init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """
    A formatter that allows colors to be placed in the format string.
    Intended to help in creating more readable logging output.
    """
    COLORS = {
        "INFO":     Fore.GREEN,
        "WARNING":  Fore.YELLOW,
        "ERROR":    Fore.RED,
        "CRITICAL": Back.RED,
    }

    def format(self, record: logging.LogRecord) -> str:
        """Customize the message format based on the log level."""
        message = super().format(record)
        my_color = self.COLORS.get(record.levelname, "")
        return my_color + message


default_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "()": ColoredFormatter,
            "format": "[%(levelname)s] — %(message)s",
        },
        "extended": {
            "format": "%(asctime)s :: [%(levelname)s] :: %(funcName)s in %(filename)s (l:%(lineno)d) :: %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "stream": sys.stdout,
        },
        "local_file_handler": {
            "class": "logging.FileHandler",
            "formatter": "extended",
            "level": "ERROR",
            "filename": "debug.log",
            "mode": "w",
            "encoding": "utf8",
        },
    },
    "loggers": {
        # Root logger
        "": {
            "level": "DEBUG",
            "handlers": ["local_file_handler", 'console'],
        },
        # TODO: Fine-grained logging configuration for individual modules or classes
        #  Use this to set different log levels without changing "real" code.
        # "user_messages": {
        #     "level": "INFO",
        #     "propagate": False,
        #     "handlers": ["console"]
        # }
    },
}


def setup_logging():
    """
    Setup logging configuration
    Call this only once from the application main() function or __main__ module
    """
    logging.config.dictConfig(default_config)
