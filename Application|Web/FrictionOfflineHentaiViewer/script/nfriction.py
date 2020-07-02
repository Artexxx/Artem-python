#!/usr/bin/env python3

from os import environ
import logging

from nfriction import app

if __name__ == '__main__':
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.WARNING)

    host = environ.get('FH', '127.0.0.1')
    port = int(environ.get('FP', '5000'))

    print('listening on http://{host}:{port}/, press ctrl+c to quit'
          .format(**locals()))

    app.run(host=host, port=port)
