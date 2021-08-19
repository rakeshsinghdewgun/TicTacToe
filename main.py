from random import randint


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    while True:
        marker = input('Player 1 choose X or O:').upper().strip()
        if marker in ('X', 'O'):

            if marker == 'X':
                return 'X', 'O'

            else:
                return 'O', 'X'


def place_marker(board, position, marker):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    flip = randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    choice = 0
    while choice not in (1, 2, 3, 4, 5, 6, 7, 8, 9) or not space_check(board, choice):
        choice = int(input("Choose a position to place (1-9): "))

    return choice


def replay():
    while True:
        replay_quest = input("Want to replay? Enter 'YES' or 'NO': ").upper().strip()

        if replay_quest in ('YES', 'NO'):
            return replay_quest


def main_game():
    print('Welcome to TicTacToe!!')

    while True:

        the_board = [' '] * 10

        player_1, player_2 = player_input()
        turn = choose_first()
        print(turn + ' will go first!')

        play_game = input("Do you want to play? Enter 'YES' or 'NO: ").strip().upper()

        if play_game == 'YES':
            game_on_choice = True
        else:
            game_on_choice = False

        while game_on_choice:

            if turn == 'Player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, position, player_1)

                if win_check(the_board, player_1):
                    display_board(the_board)
                    print('Player 1 has won')
                    game_on_choice = False

                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Game tied!!')
                        game_on_choice = False

                    else:
                        turn = 'Player 2'

            else:
                if turn == 'Player 2':
                    display_board(the_board)
                    position = player_choice(the_board)
                    place_marker(the_board, position, player_2)

                    if win_check(the_board, player_2):
                        display_board(the_board)
                        print('Player 2 has won')
                        game_on_choice = False

                    else:
                        if full_board_check(the_board):
                            display_board(the_board)
                            print('Game tied!!')
                            game_on_choice = False

                        else:
                            turn = 'Player 1'

        if replay() == 'NO':
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
