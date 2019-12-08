#!/usr/bin/env python
from lib.actor import Actor, build_vehicle, build_camera
from lib.environement import Environment
from lib.lib_loader import load_lib
from lib.lib_loader import CARLA_LIB
from lib.logger import initialize_logger
from lib.pygame_manager import PyGameManager
from lib.vehicle import Vehicle

load_lib(CARLA_LIB)

from carla import Client, VehicleControl, Transform, Location

SCREEN_SIZE = (1024, 768)
APP_NAME = 'client'


def save(image):
    image.save_to_disk('output/%06d.png' % image.frame)


def connect_to_server_and_get_world():
    client = Client('localhost', 2000)
    client.set_timeout(10.0)
    return client.get_world()


def loop(game):
    pass


actors = []
logger = initialize_logger(APP_NAME)

try:
    world = connect_to_server_and_get_world()
    env = Environment(world, APP_NAME, SCREEN_SIZE)
    env.init()
    env.loop(loop)
finally:
    env.close()
