import random
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
    window = 700
    window_res = (700, 700)
    tile_size = 35
    range = (tile_size // 2, window - tile_size // 2, tile_size)
    get_random_position = lambda: [random.randrange(*range), random.randrange(*range)]
    snake = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
    snake.center = get_random_position()
    length = 1
    score = 0
    high_score = 0
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
                if event.key == pygame.K_w and dirs[pygame.K_w]:
                    snake_dir = (0, -tile_size)
                    dirs = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
                if event.key == pygame.K_s and dirs[pygame.K_s]:
                    snake_dir = (0, tile_size)
                    dirs = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
                if event.key == pygame.K_a and dirs[pygame.K_a]:
                    snake_dir = (-tile_size, 0)
                    dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
                if event.key == pygame.K_d and dirs[pygame.K_d]:
                    snake_dir = (tile_size, 0)
                    dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
        black = pygame.Color(0, 0, 0)
        green = pygame.Color(0, 200, 0)
        red = pygame.Color(200, 0, 0)
        screen.fill(black)
        # check border or self eating / restart
        selfeating = pygame.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or selfeating:
            snake.center, food.center = get_random_position(), get_random_position()
            if high_score < score:
                high_score = score
            length, snake_dir, score = 1, (0,0), 0
            segments = [snake.copy()]
        # check food
        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
            score += 1
        # draw food
        pygame.draw.rect(screen, red, food)
        #create current score
        smallfont = pygame.font.SysFont("comicsansms", 25)
        score_text = smallfont.render("Score: " + str(score), True, pygame.Color(255, 255, 255))
        screen.blit(score_text, (0,0))
        #create high score
        high_score_text = smallfont.render("High Score: " + str(high_score), True, pygame.Color(255, 255, 255))
        screen.blit(high_score_text, (200, 0))
        # draw snake
        for segment in segments:
            pygame.draw.rect(screen, green, segment)
        # move snake
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