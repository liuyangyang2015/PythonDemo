# from com.demo import dict
import logging
# from logging.config import fileConfig
logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.getLogger(__name__).addHandler(logging.NullHandler())
print(__name__)
print('hi')
logging.warning('hihi')
logging.info('watch out')