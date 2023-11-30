import random
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    window = 600
    window_res = (700, 700)
    tile_size = 40
    range = (tile_size // 2, window - tile_size // 2, tile_size)
    get_random_position = lambda: [random.randrange(*range), random.randrange(*range)]
    snake = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    snake_dir = (0,0)
    food = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
    food.center = get_random_position()
    time, time_step = 0, 110
    screen = pygame.display.set_mode(window_res)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake_dir = (0, -tile_size)
                if event.key == pygame.K_s:
                    snake_dir = (0, tile_size)
                if event.key == pygame.K_a:
                    snake_dir = (-tile_size, 0)
                if event.key == pygame.K_d:
                    snake_dir = (tile_size, 0)
        black = pygame.Color(0, 0, 0)
        green = pygame.Color(0, 200, 0)
        red = pygame.Color(200, 0, 0)
        screen.fill(black)
        pygame.draw.rect(screen, red, food)
        for segment in segments:
            pygame.draw.rect(screen, green, segment)
        time_now = pygame.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()