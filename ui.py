import pygame

pygame.init()

current_size = (300, 300)
third_size = (100, 100)

screen = pygame.display.set_mode((current_size), pygame.RESIZABLE)
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()


def update_dimensions(new_size):
    global current_size, third_size
    pygame.display.set_mode(new_size, pygame.RESIZABLE)
    current_size = screen.get_size()
    third_size = (current_size[0] // 3), (current_size[1] // 3)


GRID_THICKNESS = 4
GRID_COLOR = (0,0,0)
def draw_game():
    current_w, current_h = current_size
    third_w, third_h = third_size

    pygame.draw.line(screen, GRID_COLOR, (third_w, 0), (third_w, current_h), GRID_THICKNESS)
    pygame.draw.line(screen, GRID_COLOR, (third_w * 2, 0), (third_w * 2, current_h), GRID_THICKNESS)
    pygame.draw.line(screen, GRID_COLOR, (0, third_h), (current_w, third_h), GRID_THICKNESS)
    pygame.draw.line(screen, GRID_COLOR, (0, third_h * 2), (current_w, third_h * 2), GRID_THICKNESS)


def draw_player(letter, pos):
    pass


running = True
while running:
    for event in pygame.event.get():
        # check for pygame.QUIT
        if event.type == pygame.QUIT:
            running = False

        # check for screen resize
        elif event.type == pygame.VIDEORESIZE:
            update_dimensions(event.size)

    # wipe last frame
    screen.fill((255,255,255))

    # draw, then flip() the display
    draw_game()
    pygame.display.flip()

    clock.tick(60) 
pygame.quit()
