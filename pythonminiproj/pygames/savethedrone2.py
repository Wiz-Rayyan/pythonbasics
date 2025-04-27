import pygame
import random
import math
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Drone Survival")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

# Clock and timing
clock = pygame.time.Clock()
FPS = 60

# Game variables
NUM_BOIDS = 20
BOID_SPEED = 2

HEALTH_MAX = 100
CLOUD_COUNT = 5
LEADER_RATIO = 0.2

# Highscore file
HIGHSCORE_FILE = "highscore.txt"
if not os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, 'w') as f:
        f.write("0")

# Utility functions
def get_highscore():
    with open(HIGHSCORE_FILE, 'r') as f:
        return int(f.read())

def save_highscore(score):
    with open(HIGHSCORE_FILE, 'w') as f:
        f.write(str(score))

# Boid class
class Boid:
    def __init__(self, x, y, is_leader=False):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.is_leader = is_leader

    def update(self, leader=None):
        if leader and not self.is_leader:
            dx = leader.x - self.x
            dy = leader.y - self.y
            dist = math.hypot(dx, dy)
            if dist > 0:
                self.vx += (dx / dist) * 0.05
                self.vy += (dy / dist) * 0.05

        speed = math.hypot(self.vx, self.vy)
        if speed > 0:
            self.vx = (self.vx / speed) * BOID_SPEED
            self.vy = (self.vy / speed) * BOID_SPEED

        self.x += self.vx
        self.y += self.vy

        if self.x < 0: self.x = WIDTH
        if self.x > WIDTH: self.x = 0
        if self.y < 0: self.y = HEIGHT
        if self.y > HEIGHT: self.y = 0

    def draw(self):
        color = RED if self.is_leader else BLACK
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 6)

# Cloud class
class Cloud:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT // 2)
        self.speed = random.uniform(0.2, 0.6)

    def update(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -100
            self.y = random.randint(0, HEIGHT // 2)

    def draw(self):
        pygame.draw.ellipse(screen, GRAY, (self.x, self.y, 120, 60))

# Drone class
class Drone:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.health = HEALTH_MAX
        self.dragging = False

    def handle_mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if abs(mx - self.x) < 20 and abs(my - self.y) < 20:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.x, self.y = event.pos
            self.x = max(0, min(WIDTH, self.x))
            self.y = max(0, min(HEIGHT, self.y))

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x - 15, self.y - 15, 30, 30))

# Collision detection
def check_collisions(drone, boids):
    for boid in boids:
        dist = math.hypot(drone.x - boid.x, drone.y - boid.y)
        if dist < 20:
            drone.health -= 1
            return

# Game reset
def reset_game():
    return [Boid(random.randint(0, WIDTH), random.randint(0, HEIGHT), i < NUM_BOIDS * LEADER_RATIO) for i in range(NUM_BOIDS)], Drone(), [Cloud() for _ in range(CLOUD_COUNT)], 0

# Main game loop
def main():
    boids, drone, clouds, score = reset_game()
    running = True
    game_over = False
    highscore = get_highscore()
    start_ticks = pygame.time.get_ticks()

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_over:
                drone.handle_mouse(event)

        if not game_over:
            for cloud in clouds:
                cloud.update()
                cloud.draw()

            leaders = [b for b in boids if b.is_leader]
            followers = [b for b in boids if not b.is_leader]

            for leader in leaders:
                leader.update()
                leader.draw()

            for follower in followers:
                nearest_leader = min(leaders, key=lambda l: math.hypot(follower.x - l.x, follower.y - l.y))
                follower.update(nearest_leader)
                follower.draw()

            drone.draw()
            check_collisions(drone, boids)

            pygame.draw.rect(screen, RED, (10, 10, 200, 20))
            pygame.draw.rect(screen, BLUE, (10, 10, 200 * (drone.health / HEALTH_MAX), 20))

            seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            score = seconds
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 40))

            if drone.health <= 0:
                game_over = True
                if score > highscore:
                    save_highscore(score)
                    highscore = score
        else:
            keys = pygame.key.get_pressed()
            game_over_text = big_font.render("GAME OVER", True, RED)
            restart_text = font.render("Press R to Restart", True, BLACK)
            high_text = font.render(f"High Score: {highscore}", True, BLACK)
            screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2 - 60))
            screen.blit(restart_text, (WIDTH//2 - 130, HEIGHT//2))
            screen.blit(high_text, (WIDTH//2 - 100, HEIGHT//2 + 40))

            if keys[pygame.K_r]:
                boids, drone, clouds, score = reset_game()
                game_over = False
                start_ticks = pygame.time.get_ticks()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
