'''
basicConfig
  filename='example.log',
  encoding='utf-8',
  level=logging.DEBUG
  format='%(levelname)s:
          %(message)s:
          %(name)s:
          %(asctime)s':
          (%(filename)s).%(funcName)s(%(lineno)d)
  datefmt='%m/%d/%Y %I:%M:%S %p'
'''

import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='w', format='%(asctime)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(name)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)