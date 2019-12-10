import logging
import random
from enum import Enum

from carla.libcarla import Transform


class Actor(Enum):
    TESLA_MODEL_3 = 'model3'
    RGB_CAMERA = 'sensor.camera.rgb'
    COLLISION_SENSOR = 'sensor.other.collision'


class ActorBuilder:
    def __init__(self, world, name, logger=logging.getLogger('client')):
        blueprint_library = world.get_blueprint_library()
        self.__blue_print = blueprint_library.filter(name.value)[0]
        self.__world = world
        self.__spawn_point = None
        self.__attach_to = None
        self.__logger = logger

    def attr(self, name, value):
        self.__blue_print.set_attribute(name, str(value))
        return self

    def spawn_point(self, point):
        self.__spawn_point = point
        return self

    def random_spawn_point(self):
        self.spawn_point(random.choice(self.__world.get_map().get_spawn_points()))
        return self

    def attach_to(self, actor):
        self.__attach_to = actor
        return self

    def build(self):
        self.__log()
        return self.__world.spawn_actor(self.__blue_print, self.__spawn_point, attach_to=self.__attach_to)

    def __log(self):
        output = f"Spawning '{self.__blue_print.id}' actor: \n\t- {self.__spawn_point.location}\n\t- {self.__spawn_point.rotation}"
        if self.__attach_to is not None:
            output += f"\n\t- Attached to: '{self.__attach_to.type_id}' actor."
        self.__logger.info(output)


def build_vehicle(world, actor_name):
    return ActorBuilder(world, actor_name) \
        .random_spawn_point() \
        .build()


def build_collision_sensor(world, vehicle, location):
    return ActorBuilder(world, Actor.COLLISION_SENSOR) \
        .spawn_point(Transform(location)) \
        .attach_to(vehicle.wrapped()) \
        .build()


def build_camera(world, screen_size, vehicle, location):
    return ActorBuilder(world, Actor.RGB_CAMERA) \
        .attr('image_size_x', screen_size[0]) \
        .attr('image_size_y', screen_size[1]) \
        .attr('fov', 110) \
        .attr('sensor_tick', 0.0) \
        .attr('gamma', 2.2) \
        .spawn_point(Transform(location)) \
        .attach_to(vehicle.wrapped()) \
        .build()
