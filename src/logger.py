import logging
from datetime import datetime
import os


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ##creates log file name
logspath = os.path.join(os.getcwd(),"logs",LOG_FILE)  
os.makedirs(logspath,exist_ok=True)
LOG_FILE_PATH = os.path.join(logspath,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO ##severity less than info will be ignored

)

if __name__ == "__main__":
    logging.info("Logging has started")