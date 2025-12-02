import logging
import os
from datetime import datetime, timedelta

def setup_logging():
    log_filename = "application.log"
    
    # Check if log file exists and is older than 1 day
    if os.path.exists(log_filename):
        try:
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(log_filename))
            if datetime.now() - file_mod_time > timedelta(days=1):
                os.remove(log_filename)
                print(f"Deleted old log file: {log_filename}")
        except Exception as e:
            print(f"Error checking/deleting log file: {e}")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()
