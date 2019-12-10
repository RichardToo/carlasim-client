from carla.libcarla import Client


class CarlaClient:

    def __init__(self, uri='localhost', port=2000, timeout=10):
        self.__client = Client(uri, port)
        self.__client.set_timeout(timeout)

    def get_world(self): return self.__client.get_world()
