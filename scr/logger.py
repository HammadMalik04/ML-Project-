import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_folder = os.path.join(os.getcwd(), "logs",LOG_FILE)  # Path to the logs directory
os.makedirs(logs_folder, exist_ok=True)  # Ensure the logs directory exists

LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)  # Path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)




if __name__=="__main__":
    logging.info("logging has started")