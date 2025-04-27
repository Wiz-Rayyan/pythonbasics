import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")

# Constants
NUM_BOIDS = 30
MAX_SPEED = 4
MAX_FORCE = 0.05
PERCEPTION_RADIUS = 50

# Colors
WHITE = (255, 255, 255)
BOID_COLOR = (100, 200, 255)

# Vector class shortcut
vec = pygame.math.Vector2

class Boid:
    def __init__(self):
        self.position = vec(random.uniform(0, WIDTH), random.uniform(0, HEIGHT))
        angle = random.uniform(0, 2 * math.pi)
        self.velocity = vec(math.cos(angle), math.sin(angle))
        self.acceleration = vec(0, 0)

    def edges(self):
        if self.position.x > WIDTH: self.position.x = 0
        elif self.position.x < 0: self.position.x = WIDTH
        if self.position.y > HEIGHT: self.position.y = 0
        elif self.position.y < 0: self.position.y = HEIGHT

    def align(self, boids):
        steering = vec(0, 0)
        total = 0
        for other in boids:
            if other != self and self.position.distance_to(other.position) < PERCEPTION_RADIUS:
                steering += other.velocity
                total += 1
        if total > 0:
            steering /= total
            steering = steering.normalize() * MAX_SPEED
            steering -= self.velocity
            if steering.length() > MAX_FORCE:
                steering.scale_to_length(MAX_FORCE)
        return steering

    def cohesion(self, boids):
        steering = vec(0, 0)
        total = 0
        for other in boids:
            if other != self and self.position.distance_to(other.position) < PERCEPTION_RADIUS:
                steering += other.position
                total += 1
        if total > 0:
            steering /= total
            steering -= self.position
            steering = steering.normalize() * MAX_SPEED
            steering -= self.velocity
            if steering.length() > MAX_FORCE:
                steering.scale_to_length(MAX_FORCE)
        return steering

    def separation(self, boids):
        steering = vec(0, 0)
        total = 0
        for other in boids:
            distance = self.position.distance_to(other.position)
            if other != self and distance < PERCEPTION_RADIUS / 2:
                diff = self.position - other.position
                diff /= distance
                steering += diff
                total += 1
        if total > 0:
            steering /= total
            steering = steering.normalize() * MAX_SPEED
            steering -= self.velocity
            if steering.length() > MAX_FORCE:
                steering.scale_to_length(MAX_FORCE)
        return steering

    def update(self, boids):
        self.acceleration = vec(0, 0)
        self.acceleration += self.align(boids)
        self.acceleration += self.cohesion(boids)
        self.acceleration += self.separation(boids)

        self.velocity += self.acceleration
        if self.velocity.length() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)
        self.position += self.velocity
        self.edges()

    def draw(self, screen):
        # Draw triangle for boid
        angle = self.velocity.angle_to(vec(1, 0))
        points = [vec(10, 0), vec(-5, 5), vec(-5, -5)]
        rotated_points = [self.position + p.rotate(-angle) for p in points]
        pygame.draw.polygon(screen, BOID_COLOR, rotated_points)

# Create boids
boids = [Boid() for _ in range(NUM_BOIDS)]

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for boid in boids:
        boid.update(boids)
        boid.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
