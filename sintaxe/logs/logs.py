# The logging module is a ready-to-use module that allows you to log messages in your application.

import logging

# create logger
logging.basicConfig(filename='sintaxe/logs/test.log', level=logging.DEBUG,filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 'application' code
logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')

# Output:
# 2024-02-12 21:08:36,077 - root - DEBUG - debug message
# 2024-02-12 21:08:36,077 - root - INFO - info message
# 2024-02-12 21:08:36,077 - root - WARNING - warn message
# 2024-02-12 21:08:36,077 - root - ERROR - error message
# 2024-02-12 21:08:36,077 - root - CRITICAL - critical message