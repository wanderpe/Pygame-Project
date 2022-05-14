import pygame, sys
class Window(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 600))
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill("black")
            pygame.display.flip()


if __name__ == "__main__":
    window = Window()
    window.game_loop()




