# from com.demo import dict
import logging
# from logging.config import fileConfig
logger = logging.getLogger('com.bigroad.python.demo.test21')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='example.log',level=logging.DEBUG)
# logging.getLogger(__name__).addHandler(logging.NullHandler())
print(__name__)
print('hi')
logging.warning('hihi')
logger.info('watch out')

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)