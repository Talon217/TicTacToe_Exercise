import pygame
from config import LINE_COLOR, LINE_THICKNESS


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

    def draw_x(self, row: int, col: int) -> None:
        ...

    def draw_o(self, row: int, col: int) -> None:
        ...

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