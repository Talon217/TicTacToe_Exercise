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


def win_check():
    for i in range(3):
        # Rows
        if grid[i][0] == grid[i][1] == grid[i][2] != "":
            show_win(grid[i][0], "row", i)
            return True
        
        # Columns
        if grid[0][i] == grid[1][i] == grid[2][i] != "":
            show_win(grid[0][i], "col", i)
            return True

    # Diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        show_win(grid[1][1], "tl2br", None)
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        show_win(grid[1][1], "tr2bl", None)
        return True

    return False


def show_win(letter, line_type, line_num):
    current_w, current_h = current_size
    third_w, third_h = third_size
    if letter == "x":
        win_color = X_COLOR
    else:
        win_color = O_COLOR

    if line_type == "row":
        # Center Y of the winning row
        center_y = round((third_h / 2) + line_num * third_h)
        start_pos = (0, center_y)
        end_pos = (current_w, center_y)

    elif line_type == "col":
        # Center X of the winning column
        center_x = round((third_w / 2) + line_num * third_w)
        start_pos = (center_x, 0)
        end_pos = (center_x, current_h)

    elif line_type == "tl2br":
        # Top-Left corner to Bottom-Right corner
        start_pos = (0, 0)
        end_pos = (current_w, current_h)

    elif line_type == "tr2bl":
        # Top-Right corner to Bottom-Left corner
        start_pos = (current_w, 0)
        end_pos = (0, current_h)

    # Draw line across the winning cells
    pygame.draw.line(screen, win_color, start_pos, end_pos, LINE_THICKNESS*2)


# main game loop
running = True
win = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            update_dimensions(event.size)

        # initiate turn on mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if win:
                grid = [
                    ["", "", ""], # row 1
                    ["", "", ""], # row 2
                    ["", "", ""]  # row 3
                ]
                win = False
            player = player_turn(player, event.pos)

    screen.fill((255,255,255))
    render_background()
    render_plays()
    win = win_check()
    pygame.display.flip()

    clock.tick(60) 
pygame.quit()
