import math
import time
import random
import pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Initialize the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIM TRAINER")

# Target properties
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

# Target class
class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = (255, 0, 0)  # Red
    SECOND_COLOR = (255, 255, 255)  # White

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), int(self.size * 0.8))
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size * 0.6))
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), int(self.size * 0.4))

# Draw function
def draw(win, targets):
    win.fill((0, 0, 0))  # Black background

    for target in targets:
        target.draw(win)

    pygame.display.update()

# Main function
def main():
    run = True
    targets = []

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

        for target in targets:
            target.update()

        draw(WIN, targets)

    pygame.quit()

if __name__ == "__main__":
    main()
