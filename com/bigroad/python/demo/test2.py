# from com.demo import dict
import logging
# from logging.config import fileConfig
logger = logging.getLogger('com.bigroad.python.demo.test2')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='example.log',level=logging.DEBUG)
# logging.getLogger(__name__).addHandler(logging.NullHandler())
print(__name__)
print('hi')
logging.warning('hihi')
logger.info('watch out')