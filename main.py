import pygame
from pygame.locals import *
import math


pygame.init()

WIDTH = HEIGHT = 640
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('UCM')

FPS = 60
timer = pygame.time.Clock()

running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (240, 20, 20)
BLUE = (20, 20, 240)
RADIUS = 200
CENTER = (640 / 2, 640 / 2)


class Ball:
    def __init__(self):
        self.color = RED
        self.initial_pos = (640 / 2, 640 / 2 - RADIUS)
        self.pos_x = self.initial_pos[0]
        self.pos_y = self.initial_pos[1]
        self.main_radius = RADIUS
        self.radius = self.main_radius / 10
        self.particle = pygame.draw.circle(WINDOW, self.color, self.initial_pos, self.radius)
        self.angle = 0
        self.velocity = 5
        self.angular_speed = self.velocity / self.main_radius
        self.velocity_x = 0
        self.velocity_y = 0

    def tick(self):
        self.angle += self.angular_speed
        self.velocity_x = math.cos(self.angle) * self.velocity
        self.velocity_y = math.sin(self.angle) * self.velocity
        self.particle = pygame.draw.circle(WINDOW, self.color, (self.pos_x, self.pos_y), self.radius)
        self.pos_x += self.velocity_x
        self.pos_y += self.velocity_y
        print(self.distance_to_center())

    def distance_to_center(self):
        main_center = CENTER
        dx = main_center[0] - self.pos_x
        dy = main_center[1] - self.pos_y
        x = math.sqrt(dx ** 2 + dy ** 2)
        return x


ball = Ball()

while running:
    WINDOW.fill(BLACK)
    timer.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False

    if not running:
        break

    main_circle = pygame.draw.circle(WINDOW, RED, CENTER, radius=RADIUS, width=1)
    ball.tick()

    pygame.display.flip()
