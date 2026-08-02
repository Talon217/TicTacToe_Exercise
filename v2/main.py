import pygame
from logic import Logic
from ui import UI


def main() -> None:
    view = UI()
    model = Logic()

    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running: bool = False

            elif event.type == pygame.VIDEORESIZE:
                view.window_resized()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                row, col = view.clicked_cell(event.pos)
                model.make_move(row, col)

        view.screen.fill((255,255,255))
        view.draw_grid()

        pygame.display.flip()

        view.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()