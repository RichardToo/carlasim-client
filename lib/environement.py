import logging
import time

from carla.libcarla import Location

from lib.actor import build_camera, build_vehicle, Actor, build_collision_sensor
from lib.pygame_manager import PyGameManager
from lib.vehicle import Vehicle


class Environment:
    def __init__(self, world, app_name, screen_size):
        self.__world = world
        self.__screen_size = screen_size
        self.__logger = logging.getLogger(app_name)
        self.__game = PyGameManager(app_name, screen_size)
        self.vehicle = None
        self.camera = None
        self.collision_sensor = None
        self.collision = False
        self.__actors = []
        self.__logger.info("Create environment...")
        self.__init()
        self.__colliding = False

    def __init(self):
        self.vehicle = Vehicle(
            build_vehicle(
                self.__world,
                Actor.TESLA_MODEL_3
            )
        )
        self.vehicle.control(throttle=1.0, steer=0.0)
        self.__game.vehicle(self.vehicle)

        location = Location(x=1.1, z=1.2)

        self.camera = build_camera(
            self.__world,
            self.__screen_size,
            self.vehicle,
            location
        )
        self.camera.listen(self.__game.render)

        self.collision_sensor = build_collision_sensor(self.__world, self.vehicle, location)

        self.collision_sensor.listen(lambda event: self.__on_collision(event))

        self.__actors = [self.camera, self.vehicle.wrapped(), self.collision_sensor]

    def reset(self):
        self.__logger.info("Random vehicle relocation...")
        self.vehicle.random_location(self.__world)

    def loop(self, callback):
        self.__game.loop(lambda game: self.__loop(game, callback))

    def __loop(self, game, callback):
        callback(self)

    def close(self):
        self.__destroy_actors()
        self.__game.quit()

    def __destroy_actors(self):
        for actor in self.__actors:
            if actor is not None:
                self.__logger.info(f"Destroy {actor}")
                actor.destroy()

    def __on_collision(self, event):
        if not self.__colliding:
            self.__colliding = True
            self.__logger.info("Vehicle collide...")
            time.sleep(1)
            self.reset()
            self.__colliding = False
