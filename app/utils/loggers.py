import logging
from datetime import datetime


def get_logger(name: str = "logger"):
    new_logger = logging.getLogger(name)
    formatter = logging.Formatter("%(asctime)s || %(levelname)s || %(message)s",
                                  "%Y-%m-%d %H:%M:%S")

    new_logger.setLevel(logging.DEBUG)
    dev_fh = logging.FileHandler('logs/{:%Y-%m-%d}-dev.log'.format(datetime.now()))
    dev_fh.setLevel(logging.DEBUG)
    dev_fh.setFormatter(formatter)
    game_fh2 = logging.FileHandler('logs/{:%Y-%m-%d}-game.log'.format(datetime.now()))
    game_fh2.setLevel(logging.INFO)
    game_fh2.setFormatter(formatter)
    new_logger.addHandler(dev_fh)
    new_logger.addHandler(game_fh2)
    return new_logger


logger = get_logger()
