import numpy as np
from carla.libcarla import VehicleControl


class Vehicle:
    def __init__(self, vehicle):
        self.__vehicle = vehicle

    def speed(self):
        v = self.__vehicle.get_velocity()
        return int(3.6 * np.math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2))

    def control(self, throttle, steer):
        self.__vehicle.apply_control(VehicleControl(throttle=throttle, steer=steer))

    def wrapped(self):
        return self.__vehicle
