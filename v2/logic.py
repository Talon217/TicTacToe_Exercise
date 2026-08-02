class Logic:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.grid = [
            ["", "", ""], # row 1
            ["", "", ""], # row 2
            ["", "", ""]  # row 3
        ]
        self.current_player = "x"

    def make_move(self, row: int, col: int) -> None:
        #clamp error check
        if row > 2 or row < 0 or col > 2 or col < 0:
            return
    
        if self.grid[row][col] == "":
            self.grid[row][col] = self.current_player
            self.switch_player()

    def switch_player(self) -> None:
        self.current_player = "o" if self.current_player == "x" else "x"

    def win_check(self) -> str:
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != "":
                return f"{row[0].upper()} Wins!"

        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != "":
                return f"{self.grid[0][col].upper()} Wins!"

        #check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[1][1] != "":
            return f"{self.grid[1][1].upper()} Wins!"
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[1][1] != "":
            return f"{self.grid[1][1].upper()} Wins!"

    def is_board_full(self) -> bool:
        for row in self.grid:
            if "" in row:
                return False
        return True