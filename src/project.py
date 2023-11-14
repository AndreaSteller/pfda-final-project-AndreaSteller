import random
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    window = 900
    window_res = (900, 900)
    tile_size = 50
    range = (tile_size // 2, window - tile_size // 2, tile_size)
    get_random_position = lambda: [random.randrange(*range), random.randrange(*range)]
    snake = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    screen = pygame.display.set_mode(window_res)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        green = pygame.Color(0, 200, 0)
        screen.fill(black)
        for segment in segments:
            pygame.draw.rect(screen, green, segment)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()