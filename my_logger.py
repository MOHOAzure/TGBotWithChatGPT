import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

f_handler = logging.FileHandler('app_failure.log')
f_handler.setLevel(logging.ERROR)
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
