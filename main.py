from random import choice

xod = 1
winning_coord_player1 = []
winning_coord_player2 = []
x_turn = 0
player1_win = False
player2_win = False
game_draw = False


def best_move(empty_slots, board, len_for_win):
    global x_turn
    score = 0
    lst = []

    for moves in empty_slots:
        board[moves[0]][moves[1]] = 'X'
        if check_board(board, empty_slots, len_for_win, True, check_player2=True):
            board[moves[0]][moves[1]] = '.'
            score += 1000
            lst.append((score, moves))
            return lst
        lst.append((x_turn, moves))

        new_empty = empty_slots.copy()
        new_empty.remove(moves)

        for opponent_moves in new_empty:
            board[opponent_moves[0]][opponent_moves[1]] = '0'
            if check_board(board, empty_slots, len_for_win, True, check_player1=True):
                try:
                    lst.remove((x_turn, moves))
                except ValueError:
                    continue
            board[opponent_moves[0]][opponent_moves[1]] = '.'
        board[moves[0]][moves[1]] = '.'
        x_turn = 0

    return lst


def who_win():
    if player1_win:
        print(f'player1 -win\nwinning combination - {winning_coord_player1}')
    elif player2_win:
        print(f'player2 -win\nwinning combination - {winning_coord_player2}')
    else:
        print('DRAW')


def draw_board(board):
    for i in board:
        print(i)


def player1_move(board, empty_slots, len_for_win):
    global xod
    if not xod == 1:
        try:
            lst = sorted(best_move(empty_slots, board, len_for_win), key=lambda score: score[0])
            move = lst[-1][1]
        except IndexError:
            move = choice(list(empty_slots))
    if xod == 1:
        move = choice(list(empty_slots))
        xod = 2
    board[move[0]][move[1]] = 'X'
    empty_slots.discard((move[0], move[1]))
    print(f'player1 turn - {(move[0], move[1])}')


def player2_move(board, empty_slots):
    move = choice(list(empty_slots))
    board[move[0]][move[1]] = '0'
    empty_slots.discard((move[0], move[1]))
    print(f'player2 turn - {(move[0], move[1])}')


def check_draw(empty_slots):
    global game_draw
    if not empty_slots:
        game_draw = True

        return True
    return False


def check_win(win_player1, win_player2, len_for_win, check=False):
    global player1_win, player2_win
    if win_player1 == len_for_win:
        if not check:
            player1_win = True
        return True
    elif win_player2 == len_for_win:
        if not check:
            player2_win = True
        return True
    return False


def check_board(board, empty_slots, len_for_win, check=False, check_player1=False, check_player2=False):
    global x_turn
    win_player1 = 0  # 'X'
    win_player2 = 0  # '0'

    # по горизонтали

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                win_player2 = 0
                win_player1 += 1
                if win_player1 > 1 and x_turn < win_player1:
                    x_turn = win_player1
                if not check:
                    winning_coord_player1.append((i, j))
                    winning_coord_player2.clear()
                if not check_player1:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True

            elif board[i][j] == '0':
                win_player1 = 0
                win_player2 += 1
                if not check:
                    winning_coord_player2.append((i, j))
                    winning_coord_player1.clear()
                if not check_player2:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            else:
                win_player1 = 0
                win_player2 = 0
                if not check:
                    winning_coord_player1.clear()
                    winning_coord_player2.clear()

        win_player1 = 0
        win_player2 = 0
        if not check:
            winning_coord_player1.clear()
            winning_coord_player2.clear()

    # по вертикали

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[j][i] == 'X':
                win_player2 = 0
                win_player1 += 1
                if win_player1 > 1 and x_turn < win_player1:
                    x_turn = win_player1
                if not check:
                    winning_coord_player1.append((j, i))
                    winning_coord_player2.clear()
                if not check_player1:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            elif board[j][i] == '0':
                win_player1 = 0
                win_player2 += 1
                if not check:
                    winning_coord_player2.append((j, i))
                    winning_coord_player1.clear()
                if not check_player2:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            else:
                win_player1 = 0
                win_player2 = 0
                if not check:
                    winning_coord_player1.clear()
                    winning_coord_player2.clear()

        win_player1 = 0
        win_player2 = 0
        if not check:
            winning_coord_player1.clear()
            winning_coord_player2.clear()

    # по диагонали
    # слева направо верхняя часть
    k = 1
    for i in range(len(board)):
        maximum_right = len(board) - i
        maximum_left = len(board)

        for j in range(len(board[i])):
            if board[j][len(board) - maximum_right] == 'X':
                maximum_right = maximum_right - 1
                win_player2 = 0
                win_player1 += 1
                if win_player1 > 1 and x_turn < win_player1:
                    x_turn = win_player1
                if not check:
                    winning_coord_player1.append((j, len(board) - maximum_right))
                    winning_coord_player2.clear()
                if not check_player1:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
                if maximum_right <= 0:
                    break
            elif board[j][len(board) - maximum_right] == '0':
                maximum_right = maximum_right - 1
                win_player1 = 0
                win_player2 += 1
                if not check:
                    winning_coord_player2.append((j, len(board) - maximum_right))
                    winning_coord_player1.clear()
                if not check_player2:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
                if maximum_right <= 0:
                    break
            else:
                maximum_right = maximum_right - 1
                win_player1 = 0
                win_player2 = 0
                if not check:
                    winning_coord_player1.clear()
                    winning_coord_player2.clear()
                if maximum_right <= 0:
                    break
        win_player1 = 0
        win_player2 = 0
        if not check:
            winning_coord_player1.clear()
            winning_coord_player2.clear()
        # слева направо нижняя часть
        for j in range(len(board[i]) - 1):
            if j + k >= len(board[i]):
                break

            if board[j + k][len(board) - maximum_left] == 'X':
                maximum_left = maximum_left - 1
                win_player2 = 0
                win_player1 += 1
                if win_player1 > 1 and x_turn < win_player1:
                    x_turn = win_player1
                if not check:
                    winning_coord_player1.append((j + k, len(board) - maximum_left))
                    winning_coord_player2.clear()
                if not check_player1:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
                if maximum_left <= 0:
                    break

            elif board[j + k][len(board) - maximum_left] == 'O':
                maximum_left = maximum_left - 1
                win_player1 = 0
                win_player2 += 1
                if not check:
                    winning_coord_player2.append((j + k, len(board) - maximum_left))
                    winning_coord_player1.clear()
                if not check_player2:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True

                if maximum_left <= 0:
                    break
            else:
                maximum_left = maximum_left - 1
                win_player1 = 0
                win_player2 = 0
                if not check:
                    winning_coord_player1.clear()
                    winning_coord_player2.clear()
                if maximum_left <= 0:
                    break
        win_player1 = 0
        win_player2 = 0
        if not check:
            winning_coord_player1.clear()
            winning_coord_player2.clear()
        k += 1

    # справа налево верхняя часть
    for i in range(len(board)):
        k = 0
        maximum_left = i
        maximum_right = i + 1
        for j in range(len(board)):
            if len(board) - maximum_left <= 0:
                break
            if board[j][len(board) - 1 - maximum_left] == 'X':
                win_player2 = 0
                win_player1 += 1
                if win_player1 > 1 and x_turn < win_player1:
                    x_turn = win_player1
                if not check:
                    winning_coord_player1.append((j, len(board) - 1 - maximum_left))
                    winning_coord_player2.clear()
                if not check_player1:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            elif board[j][len(board) - 1 - maximum_left] == '0':
                win_player1 = 0
                win_player2 += 1
                if not check:
                    winning_coord_player2.append((j, len(board) - 1 - maximum_left))
                    winning_coord_player1.clear()
                if not check_player2:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            else:
                win_player1 = 0
                win_player2 = 0
                if not check:
                    winning_coord_player1.clear()
                    winning_coord_player2.clear()

            maximum_left += 1

        win_player1 = 0
        win_player2 = 0
        # спава налево нижняя часть
        for j in range(len(board)):
            if j + maximum_right >= len(board):
                break
            if board[j + maximum_right][len(board) - 1 - k] == 'X':
                win_player2 = 0
                win_player1 += 1
                if win_player1 > 1 and x_turn < win_player1:
                    x_turn = win_player1
                if not check:
                    winning_coord_player1.append((j + maximum_right, len(board) - 1 - k))
                    winning_coord_player2.clear()
                if not check_player1:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            elif board[j + maximum_right][len(board) - 1 - k] == '0':
                win_player1 = 0
                win_player2 += 1
                if not check:
                    winning_coord_player2.append((j + len(board) - 1 - k))
                    winning_coord_player1.clear()
                if not check_player2:
                    if check_win(win_player1, win_player2, len_for_win, check):
                        return True
            else:
                win_player1 = 0
                win_player2 = 0
                if not check:
                    winning_coord_player1.clear()
                    winning_coord_player2.clear()
            k += 1
        maximum_right += 1
        win_player1 = 0
        win_player2 = 0
        if not check:
            winning_coord_player1.clear()
            winning_coord_player2.clear()

    return check_draw(empty_slots)


def game(len_for_win, board, empty_slots):
    while True:
        player1_move(board, empty_slots, len_for_win)
        draw_board(board)
        print('\n')
        if check_board(board, empty_slots, len_for_win):
            who_win()
            break

        player2_move(board, empty_slots)
        draw_board(board)
        print('\n')
        if check_board(board, empty_slots, len_for_win):
            who_win()
            break


def main():
    n = int(input('Введите размер стороны квадратного игрового поля (максимум 10):'))
    while n > 10:
        print('вы ввели слишком большое значение')
        n = int(input('Введите размер стороны квадратного игрового поля (максимум 10):'))
    len_for_win = int(input('Введите длину цепочки для победы:'))
    while len_for_win > n:
        print('размер длины цепочки для победы не должен превышать размер стороны игрового поля')
        len_for_win = int(input('Введите длину цепочки для победы:'))
    board = [['.'] * n for i in range(n)]
    empty_slots = {(i, j) for i in range(n) for j in range(n)}
    game(len_for_win, board, empty_slots)


if __name__ == '__main__':
    main()
