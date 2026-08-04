import pygame
from logic import Logic
from ui import UI


def main() -> None:
    view = UI()
    model = Logic()

    win = False
    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running: bool = False

            elif event.type == pygame.VIDEORESIZE:
                view.window_resized()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if win or model.is_board_full():
                    model.reset()
                    win = False

                row, col = view.clicked_cell(event.pos)
                model.make_move(row, col)
                

        view.screen.fill((255,255,255))
        view.draw_grid()
        view.draw_plays(model.grid)
        win_info = model.win_check()
        if win_info:
            player, line_type, line_num = win_info
            view.draw_win(player, line_type, line_num)
            win = True
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()