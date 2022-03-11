def xox_print(x):
    print(f'''---------
| {x[0][0]} {x[0][1]} {x[0][2]} |
| {x[1][0]} {x[1][1]} {x[1][2]} |
| {x[2][0]} {x[2][1]} {x[2][2]} |
---------''')


def check_win(m):
    # checking rows
    lis = [f'{m[i][0]} wins' for i in range(3) if m[i][0] == m[i][1] and m[i][0] == m[i][2]]
    # checking columns
    lis.extend([f'{m[0][i]} wins' for i in range(3) if m[0][i] == m[1][i] and m[0][i] == m[2][i]])
    lis.extend([f'{m[0][0]} wins' if m[0][0] == m[1][1] and m[0][0] == m[2][2] else None])
    lis.extend([f'{m[2][0]} wins' if m[2][0] == m[1][1] and m[2][0] == m[0][2] else None])
    return lis


def check_status(x):
    no_x = sum([1 for i in x for j in i if j == 'X'])
    no_o = sum([1 for i in x for j in i if j == 'O'])
    no_empty_cell = sum([1 for i in x for j in i if j == '_'])
    win_status = check_win(x)
    if abs(no_x - no_o) > 1 or ('X wins' in win_status and 'O wins' in win_status):
        return 'Impossible'
    elif 'X wins' in win_status:
        return 'X wins'
    elif 'O wins' in win_status:
        return 'O wins'
    elif no_empty_cell > 0:
        return 'Game not finished'
    else:
        return 'Draw'


def next_move(m, s):
    while True:
        try:
            x, y = input('Enter the coordinates: ').split()
        except ValueError:
            print('You should enter numbers!')
        else:
            if not x.isdigit() or not y.isdigit():
                print('You should enter numbers!')
            elif int(x) not in [1, 2, 3] or int(y) not in [1, 2, 3]:
                print('Coordinates should be from 1 to 3!')
            elif m[int(x) - 1][int(y) - 1] != '_':
                print('This cell is occupied! Choose another one!')
            else:
                if s == 'X':
                    m[int(x) - 1][int(y) - 1] = 'X'
                    s = 'O'
                else:
                    m[int(x) - 1][int(y) - 1] = 'O'
                    s = 'X'
                break
        continue
    return m, s


def play():
    xox = [['_' for _ in range(3)] for _ in range(3)]
    to_move = 'X'
    while True:
        xox_print(xox)
        status = check_status(xox)
        if status in ['X wins', 'O wins', 'Draw']:
            print(status)
            break
        else:
            xox, to_move = next_move(xox, to_move)


play()
