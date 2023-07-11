import os
from pathlib import Path
import logging

def getmylogger(name):
    file_formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(module)s')
    console_formatter = logging.Formatter('%(levelname)s -- %(message)s')
    
    path = Path(__file__)
    ROOT_DIR = path.parent.parent.absolute()
    logFilePath = os.path.join(ROOT_DIR, "Output/logfile.log")

    file_handler = logging.FileHandler(logFilePath,mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)
    
    return logger