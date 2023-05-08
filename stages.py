# Project: Simple Tic-Tac-Toe (Python)
# Stage 5/5: Fight!
def game_status(x):
    status = []
    cells = [j for i in x for j in i]
    status.extend([f"{x[i][0]} wins" for i in range(3) if x[i][0] == x[i][1] and x[i][0] == x[i][2]])
    status.extend([f"{x[0][i]} wins" for i in range(3) if x[0][i] == x[1][i] and x[0][i] == x[2][i]])
    status.extend([f"{x[1][1]} wins" if x[0][0] == x[1][1] == x[2][2] or x[2][0] == x[1][1] == x[0][2] else None])
    if "X wins" not in status and "O wins" not in status:
        status.extend(["Game not finished" if " " in cells else "Draw"])
    status.extend(["Impossible" if ("X wins" in status and "O wins" in status) or
                                   (abs(cells.count("X") - cells.count("O"))) > 1 else None])
    return [i for i in status if i not in [None, "  wins"]]


class SimpleTicTacToe:
    def __init__(self):
        self.xox = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        self.move = "X"

    def display(self):
        print(f"""---------
| {self.xox[0][0]} {self.xox[0][1]} {self.xox[0][2]} |
| {self.xox[1][0]} {self.xox[1][1]} {self.xox[1][2]} |
| {self.xox[2][0]} {self.xox[2][1]} {self.xox[2][2]} |
---------""")

    def next_move(self):
        while True:
            try:
                x, y = input().split()
                if (not x.isdigit()) and (not y.isdigit()):
                    raise ValueError
            except ValueError:
                print("You should enter numbers!")
            else:
                x, y = int(x), int(y)
                if 1 <= x <= 3 and 1 <= y <= 3:
                    if self.xox[x - 1][y - 1] == " ":
                        if self.move == "X":
                            self.xox[x - 1][y - 1] = "X"
                            self.move = "O"
                        elif self.move == "O":
                            self.xox[x - 1][y - 1] = "O"
                            self.move = "X"
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")

    def play(self):
        while True:
            self.display()
            status_game = game_status(self.xox)
            if status_game[0] == "Game not finished":
                self.next_move()
            else:
                print(status_game[0] if "Impossible" not in status_game else "Impossible")
                break


game_1 = SimpleTicTacToe()
game_1.play()
