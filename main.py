def show(xox):
    print(f'''---------
| {xox[0][0]} {xox[0][1]} {xox[0][2]} |
| {xox[1][0]} {xox[1][1]} {xox[1][2]} |
| {xox[2][0]} {xox[2][1]} {xox[2][2]} |
---------''')


def wins(xox):
    status = [f'{xox[i][0]} wins' for i in range(0, 3) if xox[i][0] == xox[i][1] and xox[i][0] == xox[i][2]]
    status.extend([f'{xox[0][i]} wins' for i in range(0, 3) if xox[0][i] == xox[1][i] and xox[0][i] == xox[2][i]])
    status.extend([f'{xox[1][1]} wins' if (xox[0][0] == xox[1][1] and xox[1][1] == xox[2][2]) or
                                          (xox[1][1] == xox[0][2] and xox[1][1] == xox[2][0]) else None])
    return status


def check_status(xox):
    status = wins(xox)
    cells = [j for i in xox for j in i]
    if abs(cells.count('X') - cells.count('O')) > 1 or 'X wins' in status and 'O wins' in status:
        return 'Impossible'
    elif ' ' in cells and ('X wins' not in status and 'O wins' not in status):
        return 'Game not finished'
    elif 'X wins' not in status and 'O wins' not in status:
        return 'Draw'
    else:
        return status[0]


def valid_move(x, y, xox):
    if not x.isdigit() or not y.isdigit():
        print('You should enter numbers!')
    elif 1 <= int(x) <= 3 and 1 <= int(y) <= 3:
        if xox[int(x) - 1][int(y) - 1] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            return True
    else:
        print('Coordinates should be from 1 to 3!')
    return False


def play():
    matrix = [[' ' for _ in range(0 + i, 3 + i)] for i in range(0, 9, 3)]
    next_move = 'X'
    while True:
        show(matrix)
        while True:
            try:
                row, column = input('Enter the coordinates: ').split()
            except ValueError:
                print('You should enter numbers!')
                continue
            if not valid_move(row, column, matrix):
                continue
            else:
                if next_move == 'X':
                    matrix[int(row) - 1][int(column) - 1] = 'X'
                    next_move = 'O'
                else:
                    matrix[int(row) - 1][int(column) - 1] = 'O'
                    next_move = 'X'
                break
        game_status = check_status(matrix)
        if game_status == 'Game not finished':
            continue
        else:
            show(matrix)
            print(game_status)
            break


play()
