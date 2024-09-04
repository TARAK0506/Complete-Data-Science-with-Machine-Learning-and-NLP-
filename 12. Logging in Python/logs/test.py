from logger import logging

def add(x, y):
    logging.debug(f'Adding {x} and {y}')
    return x + y

logging.info('Program started')
add(5,6)