#!/usr/bin/env python
from lib.carla_client import CarlaClient
from lib.environement import Environment
from lib.lib_loader import CARLA_LIB
from lib.lib_loader import load_lib
from lib.logger import initialize_logger

load_lib(CARLA_LIB)


def loop(game): pass


SCREEN_SIZE = (1280, 720)
APP_NAME = 'client'

try:
    logger = initialize_logger(APP_NAME)
    client = CarlaClient()
    env = Environment(client.get_world(), APP_NAME, SCREEN_SIZE)
    env.init()
    env.loop(loop)
finally:
    env.close()
