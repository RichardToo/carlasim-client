import logging


def initialize_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # create file handler which logs even debug messages
    fh = logging.FileHandler(f'{name}.log')
    fh.setLevel(logging.INFO)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
