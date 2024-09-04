import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y/%m/%d %H:%M:%S',
    handlers =[
        logging.FileHandler('applogger.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic App")

def add(x, y):
    logger.debug(f'Adding {x} and {y}= {x + y}')
    return x + y

def subtract(x, y):
    logger.debug(f'Subtracting {x} and {y} = {x - y}')
    return x - y

def multiply(x, y):
    logger.debug(f'Multiplying {x} and {y} = {x * y}')
    return x * y


def divide(x, y):
    try:
        result = x / y
        logger.debug(f'Dividing {x} and {y}= {result}')
        return x / y
    except ZeroDivisionError:
        logger.error('Division by zero is not allowed')
        return None
    
add(15,6)
subtract(15,6)
multiply(5,6) 
# divide(5,2)
divide(5,0)
    


