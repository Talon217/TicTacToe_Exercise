import pygame

pygame.init()

X_COLOR = (220, 20, 60)
O_COLOR = (20, 220, 180)
LINE_THICKNESS = 6
GRID_COLOR = (0,0,0)
CELL_MARGIN = .8

current_size = (300, 300)
third_size = (100, 100)
player = "x"
grid = [
    ["", "", ""], # row 1
    ["", "", ""], # row 2
    ["", "", ""]  # row 3
]

screen = pygame.display.set_mode((current_size), pygame.RESIZABLE)
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()


def update_dimensions(new_size):
    global current_size, third_size, screen
    # recreate the screen surface with the new size and store it
    screen = pygame.display.set_mode((new_size), pygame.RESIZABLE)
    current_size = screen.get_size()
    third_size = (current_size[0] // 3), (current_size[1] // 3)


def render_background():
    current_w, current_h = current_size
    third_w, third_h = third_size

    pygame.draw.line(screen, GRID_COLOR, (third_w, 0), (third_w, current_h), LINE_THICKNESS)
    pygame.draw.line(screen, GRID_COLOR, (third_w * 2, 0), (third_w * 2, current_h), LINE_THICKNESS)
    pygame.draw.line(screen, GRID_COLOR, (0, third_h), (current_w, third_h), LINE_THICKNESS)
    pygame.draw.line(screen, GRID_COLOR, (0, third_h * 2), (current_w, third_h * 2), LINE_THICKNESS)


def player_turn(player, click_pos):
    row = min(max(click_pos[1] // third_size[1], 0), 2)
    col = min(max(click_pos[0] // third_size[0], 0), 2) 

    if grid[row][col] == "":
        grid[row][col] = player
        return "x" if player == "o" else "o"

    return player


def render_plays():
    third_w, third_h = third_size
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != "":
                # calculate the center position of the cell
                center_x = round((third_w / 2) + c * third_w)
                center_y = round((third_h / 2) + r * third_h)

                if cell == "o":
                    pygame.draw.circle(screen, (O_COLOR), (center_x,center_y), min(third_size)*(CELL_MARGIN*.5), LINE_THICKNESS)

                elif cell == "x":
                    offset = min((third_w / 2)*CELL_MARGIN, (third_h / 2)*CELL_MARGIN) # value from the cell-center to the closest cell margin

                    tl = (center_x - offset, center_y - offset) # top-left cell corner
                    tr = (center_x + offset, center_y - offset) # top-right cell corner
                    bl = (center_x - offset, center_y + offset) # bottom-left cell corner
                    br = (center_x + offset, center_y + offset  ) # bottom-right cell corner

                    pygame.draw.line(screen, X_COLOR, tl, br, LINE_THICKNESS)
                    pygame.draw.line(screen, X_COLOR, tr, bl, LINE_THICKNESS)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        # check for pygame.QUIT
        if event.type == pygame.QUIT:
            running = False

        # check for screen resize
        elif event.type == pygame.VIDEORESIZE:
            update_dimensions(event.size)

        # check for player click
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
             player = player_turn(player, event.pos)


    # wipe last frame
    screen.fill((255,255,255))

    # render, then flip() the display
    render_background()
    render_plays()
    pygame.display.flip()

    clock.tick(60) 
pygame.quit()
