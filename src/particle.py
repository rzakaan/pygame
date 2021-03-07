import random
from colors import Colors


class ParticleModel:
    CIRCLE = 0,
    SQUARE = 1,
    ELLIPSE = 2,
    LINE = 3,
    FIRE = 4,


class Particle:
    def __init__(self, color=Colors.BLACK, model=ParticleModel.CIRCLE):
        self.x = 0
        self.y = 0
        self.color = color
        self.model = model


class ParticleController:
    def __init__(self, start_x, start_y, particle: Particle, density=100):
        self.start_x = start_x
        self.start_y = start_y
        self.particles = []

        for i in range(density):
            p = Particle(particle.color)
            p.x = start_x
            p.y = random.randint(0, start_y)
            p.model = particle.model
            p.color = particle.color
            self.particles.append(p)

    def set_game(self, game, screen):
        self.game = game
        self.screen = screen

    def move(self):
        self.screen.fill(Colors.WHITE)
        for particle in self.particles:
            if particle.y < 0:
                particle.x = self.start_x
                particle.y = self.start_y
            else:
                particle.y -= 1

            particle.x += random.randint(-2, 2)

            if particle.model == ParticleModel.CIRCLE:
                self.game.draw.circle(self.screen, particle.color, (particle.x, particle.y), 2)
            elif particle.model == ParticleModel.SQUARE:
                # rect(left, top, width, height)
                self.game.draw.rect(self.screen, particle.color, (particle.x, particle.y, 10, 10), 2)


        # TODO self.game.display.update()
