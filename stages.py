# Stage 3/5: What's up on the field?
def display(x):
    print(f"""---------
| {x[0][0]} {x[0][1]} {x[0][2]} |
| {x[1][0]} {x[1][1]} {x[1][2]} |
| {x[2][0]} {x[2][1]} {x[2][2]} |
---------""")


def game_status(x):
    status = []
    cells = [j for i in x for j in i]
    status.extend([f"{x[i][0]} wins" for i in range(3) if x[i][0] == x[i][1] and x[i][0] == x[i][2]])
    status.extend([f"{x[0][i]} wins" for i in range(3) if x[0][i] == x[1][i] and x[0][i] == x[2][i]])
    status.extend([f"{x[1][1]} wins" if x[0][0] == x[1][1] == x[2][2] or x[2][0] == x[1][1] == x[0][2] else None])
    if "X wins" not in status and "O wins" not in status:
        status.extend(["Game not finished" if "_" in cells else "Draw"])
    status.extend(["Impossible" if ("X wins" in status and "O wins" in status) or
                                   (abs(cells.count("X") - cells.count("O"))) > 1 else None])
    return status


xox = input()
xox = [[xox[j] for j in range(i, i + 3)] for i in range(0, 9, 3)]
display(xox)
status_game = [i for i in game_status(xox) if i is not None]
print(status_game[0] if "Impossible" not in status_game else "Impossible")
