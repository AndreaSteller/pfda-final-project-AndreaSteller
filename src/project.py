import random
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    window = 800
    screen = pygame.display.set_mode([window] * 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()