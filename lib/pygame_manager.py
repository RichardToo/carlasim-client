import numpy as np
import pygame


class PyGameManager:

    def __init__(self, window_title, scree_size):
        pygame.init()
        pygame.display.set_caption(window_title)
        self.__clock = pygame.time.Clock()
        self.__gameDisplay = pygame.display.set_mode(scree_size)
        self.__font_mid = pygame.font.Font(None, 35)
        self.__font_norm = pygame.font.Font(None, 25)
        self.__scree_size = scree_size
        self.__vehicle = None

    def vehicle(self, vehicle):
        self.__vehicle = vehicle

    def render(self, image):
        i = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
        i2 = i.reshape((self.__scree_size[1], self.__scree_size[0], 4))
        i3 = i2[:, :, :3]
        surf = pygame.surfarray.make_surface(i3)
        surf = pygame.transform.flip(surf, False, True)
        surf = pygame.transform.rotate(surf, -90)
        if surf is None:
            return

        self.__gameDisplay.blit(surf, (0, 0))

        self.render_meters()

        pygame.display.update()
        self.__clock.tick(100)

    def render_meters(self):
        self.meter("FPS", int(self.__clock.get_fps()), self.__font_norm, (20, 20))
        if self.__vehicle is not None:
            self.meter("Speed", self.__vehicle.speed(), self.__font_mid, (790, 690), postfix="Kmh")

    def meter(self, label, value, font, position=(0, 0), postfix="", color=pygame.Color('Yellow')):
        meter = font.render(f"{label}: {value} {postfix}", True, color)
        self.__gameDisplay.blit(meter, position)

    def loop(self, callback):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
            callback(self)

    def quit(self):
        pygame.quit()
