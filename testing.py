from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def divide_number(a,b):
    try:
        result=a/b
        logger.info('Dividing two numbers')
        return result
    except Exception as e:
        logger.error("Error occurred")
        raise CustomException("Customer error division by 0",sys)

if __name__=="__main__":
    try:
            logger.info("Starting main program")
            divide_number(10,0)
    except CustomException as ce:
            logger.error(str(ce))    

   
