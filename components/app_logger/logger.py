import logging
import os
import datetime

DIR = "components"
LOG_DIR = "app_logger"
LOG_SUBDIR = "main_logs"
LOG_FILE = os.path.join(os.getcwd(), DIR, LOG_DIR, LOG_SUBDIR)

os.makedirs(LOG_FILE, exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.datetime.now().strftime('%Y-%m-%d')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"


log_file_path = os.path.join(LOG_FILE, file_name)
logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.NOTSET)
