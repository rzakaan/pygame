import pygame

# Common Class
from particle import Particle, ParticleController, ParticleModel
from colors import Colors

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(Colors.GREY)

    # icon and title
    pygame.display.set_caption("Napster's Game")

    running = True
    clock = pygame.time.Clock()

    particle = Particle(Colors.GREEN, model=ParticleModel.SQUARE)
    particle_controller = ParticleController(515, 500, particle)
    particle_controller.set_game(pygame, screen)

    p2 = Particle(Colors.RED, model=ParticleModel.SQUARE)
    pc2 = ParticleController(100, 500, p2)
    pc2.set_game(pygame, screen)

    p3 = Particle(Colors.BLUE, model=ParticleModel.SQUARE)
    pc3 = ParticleController(300, 500, p3)
    pc3.set_game(pygame, screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        particle_controller.move()
        pc2.move()
        #pc3.move()
        pygame.display.flip()
        clock.tick(100)

    pygame.quit()


if __name__ == "__main__":
    main()
