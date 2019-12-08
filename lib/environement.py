import logging

from lib.actor import build_camera, build_vehicle, Actor
from lib.pygame_manager import PyGameManager
from lib.vehicle import Vehicle


class Environment:
    def __init__(self, world, app_name, screen_size):
        self.__world = world
        self.__screen_size = screen_size
        self.__logger = logging.getLogger(app_name)
        self.__game = PyGameManager(app_name, screen_size)
        self.__vehicle = None
        self.__camera = None
        self.__actors = []
        
    def init(self):
        self.__vehicle = Vehicle(build_vehicle(self.__world, Actor.TESLA_MODEL_3))
        self.__vehicle.control(throttle=5.0, steer=0.0)
        self.__game.vehicle(self.__vehicle)

        self.__camera = build_camera(self.__world, self.__screen_size, self.__vehicle)
        self.__camera.listen(self.__game.render)

        self.__actors = [self.__camera, self.__vehicle.wrapped()]

    def reset(self):
        self.init()
        self.__destroy_actors()

    def loop(self, callback):
        self.__game.loop(lambda game: callback(self))

    def close(self):
        self.__destroy_actors()
        self.__game.quit()

    def __destroy_actors(self):
        self.__logger.info('Destroying actors...')
        [actor.destroy() for actor in self.__actors]
