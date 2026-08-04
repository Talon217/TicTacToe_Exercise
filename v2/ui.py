import pygame
from config import CELL_MARGIN, LINE_COLOR, LINE_THICKNESS, O_COLOR, X_COLOR


class UI:
    def __init__(self):
        self.current_size: tuple[int, int] = [300,300]
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.current_size), pygame.RESIZABLE)
        self.split_into_thirds()

    def window_resized(self) -> None:
        self.current_size: tuple[int, int] = self.screen.get_size()
        self.split_into_thirds()

    def split_into_thirds(self) -> None:
        self.third_size: tuple[int, int] = (self.current_size[0] // 3, self.current_size[1] // 3)

    def draw_plays(self, grid: list[list[str]]) -> None:
        third_w, third_h = self.third_size
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell != "":
                    # calculate the center position of the cell
                    center_x = round((third_w / 2) + c * third_w)
                    center_y = round((third_h / 2) + r * third_h)

                    if cell == "o":
                        pygame.draw.circle(self.screen, (O_COLOR), (center_x,center_y), min(self.third_size)*(CELL_MARGIN*.5), LINE_THICKNESS)

                    elif cell == "x":
                        offset = min((third_w / 2)*CELL_MARGIN, (third_h / 2)*CELL_MARGIN) # value from the cell-center to the closest cell margin

                        tl = (center_x - offset, center_y - offset) # top-left cell corner
                        tr = (center_x + offset, center_y - offset) # top-right cell corner
                        bl = (center_x - offset, center_y + offset) # bottom-left cell corner
                        br = (center_x + offset, center_y + offset  ) # bottom-right cell corner

                        pygame.draw.line(self.screen, X_COLOR, tl, br, LINE_THICKNESS)
                        pygame.draw.line(self.screen, X_COLOR, tr, bl, LINE_THICKNESS)

    def draw_grid(self) -> None:
        t_x, t_y = self.third_size
        c_x, c_y = self.current_size

        pygame.draw.line(self.screen, LINE_COLOR, (t_x, 0), (t_x, c_y), LINE_THICKNESS) # left col line
        pygame.draw.line(self.screen, LINE_COLOR, (t_x * 2, 0), (t_x * 2, c_y), LINE_THICKNESS) # right col line
        pygame.draw.line(self.screen, LINE_COLOR, (0, t_y), (c_x, t_y), LINE_THICKNESS) # top row line
        pygame.draw.line(self.screen, LINE_COLOR, (0, t_y * 2), (c_x, t_y * 2), LINE_THICKNESS) # bottom row line

    def clicked_cell(self, click_pos: tuple[int, int]) -> tuple[int, int]:
        pixel_x, pixel_y = click_pos
        third_x, third_y = self.third_size

        col = pixel_x // third_x
        row = pixel_y // third_y

        return row, col

    def draw_win(self, player: str, line_type: str, line_num: int):
        player_color = {
            "x": X_COLOR,
            "o": O_COLOR
        }
        win_color = player_color[player.lower()]

        current_w, current_h = self.current_size
        third_w, third_h = self.third_size

        if line_type == "col":
            start_pos = (line_num * third_w + third_w // 2, 0)
            end_pos = (line_num * third_w + third_w // 2, current_h)
        if line_type == "row":
            start_pos = (0, line_num * third_h + third_h // 2)
            end_pos = (current_w, line_num * third_h + third_h // 2)
        if line_type == "tlbr":
            start_pos = (0,0)
            end_pos = (current_w, current_h)
        if line_type == "bltr":
            start_pos = (0, current_h)
            end_pos = (current_w, 0)

        pygame.draw.line(self.screen, win_color, start_pos, end_pos, LINE_THICKNESS)