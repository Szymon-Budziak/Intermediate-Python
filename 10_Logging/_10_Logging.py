import logging
"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# import helper



logger = logging.getLogger(__name__)

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# set level and the format (typically for each handler)
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('this is a warning')
logger.error('this is an error')



import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')



try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

# the same thing as above

import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error('The error is %s', traceback.format_exc())



# Rotating File Handler
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2 kB, and keep backup logs app.log.1, app.log.2, etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello world!')
"""


# Timed Rotating File Handler
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s-seconds, m-minutes, h-hours, d-days, midnight, w0 - Monday
handler = TimedRotatingFileHandler(
    'timed_test.log', when='s', interval=5, backupCount=5)  # every 5 seconds new file gets created
logger.addHandler(handler)

for _ in range(8):
    logger.info('Hello world!')
    time.sleep(5)  # sleep 5 seconds
