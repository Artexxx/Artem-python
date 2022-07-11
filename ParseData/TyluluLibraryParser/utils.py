import functools
import logging
import sys
import textwrap
import time
from pathlib import Path
from typing import Any, Union
from urllib.parse import urlsplit
from requests import HTTPError, Timeout
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

PathType = Union[str, Path]

pbar = functools.partial(tqdm, file=sys.stdout)


def logging_redirect_pbar(func):
    """
    For progress bars Inside the decorated function redirect the output after console logging,
    leaving other logging handler (e.g. log files) unaffected.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with logging_redirect_tqdm():
            return func(*args, **kwargs)

    return wrapper


def get_path(url: str) -> str:
    """
    Return the path of a URL

    Example:
    --------
    >>> get_path('https://www.example.com/test.txt')
    test.txt
    """
    return urlsplit(url).path.replace('/', '')


def _log_http_error(logger: logging.Logger, err: HTTPError) -> None:
    response = err.response
    request = err.request
    error_msg = err.args[0]
    breakpoint()
    res_text = textwrap.shorten(
        text=str(response.text),
        width=50,
        placeholder="..."
    )
    logger.error(
        "HTTP error occurred :: %s :: %s",
        error_msg,
        {
            "response": {
                "status_code": response.status_code,
                "reason": response.url,
                "text": res_text,
            },
            "request": {
                "url": request.url,
                "http_method": request.method,
                "body": request.body,
            },
        }
    )


def _log_timeout_error(logger: logging.Logger, err: Timeout) -> None:
    request = err.request
    error_msg = err.args[0]
    logger.error(
        "Timeout error occurred :: %s :: %s",
        error_msg,
        {
            "request": {
                "url": request.url,
                "http_method": request.method,
                "body": request.body,
            },
        }
    )


def ignore_http_errors(func=None):
    logger = logging.getLogger(func.__module__)

    def decorator(function):
        @functools.wraps(function)
        def wrapped(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except HTTPError as e:
                _log_http_error(logger, e)
                return None
            except Timeout as e:
                _log_timeout_error(logger, e)
                time.sleep(1)
                return wrapped(*args, **kwargs)
        return wrapped

    if not func:
        # We're called with parens.
        return decorator
    # We're called as @dataclass without parens.
    return decorator(func)
