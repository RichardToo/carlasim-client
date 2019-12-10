import pygame

from lib.image import to_rgb_array


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
        array = to_rgb_array(image)
        surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
        self.__gameDisplay.blit(surface, (0, 0))

        self.render_meters()

        pygame.display.update()
        self.__clock.tick(60)

    def render_meters(self):
        self.meter("FPS", int(self.__clock.get_fps()), self.__font_norm, (20, 20))
        if self.__vehicle is not None:
            self.meter("Speed", self.__vehicle.speed(), self.__font_mid, (20, 680), postfix="Km/h")

    def meter(self, label, value, font, position=(0, 0), postfix="", color=pygame.Color('Yellow')):
        meter = font.render(f"{label}: {value} {postfix}", True, color)
        self.__gameDisplay.blit(meter, position)

    def loop(self, callback):
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
            callback(self)

    def quit(self):
        pygame.quit()
