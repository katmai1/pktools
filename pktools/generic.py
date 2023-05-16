import toml
import logging
from time import sleep


def simpleCountdown(seconds, message="Waiting..."):
    """Simple countdown with message

    Args:
        seconds (int): Duration of countdown in seconds
        message (str, optional): Message of countdown. Defaults to "Waiting...".
    """
    while seconds > 0:
        print(f" [{seconds}] {message}", end='\r')
        seconds -= 1
        sleep(1)


def readTOML(filename):
    """Read TOML file and returns dictionary

    Args:
        filename (str): Filename path

    Returns:
        dict: Dictionary generated from file
    """
    try:
        with open(filename, 'r') as f:
            data = toml.load(f)
        return data
    except Exception as e:
        print(e)
    return None


def getLogger(name=__name__, filename="filelog.log"):
    """Generate custom logger object

    Args:
        name (str, optional): Name to use. Defaults to __name__.
        filename (str, optional): Log filename. Defaults to "filelog.log".

    Returns:
        logger: Returns Logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(filename, mode='w')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger