import random

import carla
import numpy as np
from carla.libcarla import VehicleControl, Vector3D


class Vehicle:
    def __init__(self, vehicle):
        self.__vehicle = vehicle

    def random_location(self, world):
        self.location(random.choice(world.get_map().get_spawn_points()))

    def location(self, transform):
        self.__vehicle.set_transform(transform)

    def speed(self):
        v = self.__vehicle.get_velocity()
        return int(3.6 * np.math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2))

    def control(self, throttle, steer):
        self.__vehicle.apply_control(VehicleControl(throttle=throttle, steer=steer))

    def wrapped(self):
        return self.__vehicle

    def name(self):
        return self.__vehicle.type_id
