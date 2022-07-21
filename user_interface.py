from player import Player
import random
from errors import input_error
from errors import not_positive_number_error
from errors import wrong_player_error
from errors import impossible_values_error
from errors import number_error


def ask_pencils_num() -> int:
    print('How many pencils would you like to use:')
    while True:
        try:
            number = input().strip()
            if not number.isdigit():
                raise input_error.InputError
            if number == '0':
                raise not_positive_number_error.NotPositiveNumberError
            return int(number)
        except (input_error.InputError, not_positive_number_error.NotPositiveNumberError) as error:
            print_error(error)


def ask_first_player(player_1: Player, player_2: Player) -> Player:
    print('Who will be the first ({}, {}):'.format(player_1, player_2))
    while True:
        try:
            name = input().strip()
            if player_1.name != name and player_2.name != name:
                raise wrong_player_error.WrongPlayerError(player_1.name, player_2.name)
            if player_1.name == name:
                return player_1
            return player_2
        except wrong_player_error.WrongPlayerError as error:
            print_error(error)


def print_pencils(num: int) -> None:
    print('|' * num)


def remove_num_player(name: str, pencils_num: int, player_2: Player) -> int:
    possible_numbers = {'1', '2', '3'}
    print("{}'s turn!".format(name))
    while True:
        try:
            if name != player_2.name:
                number = input()

                if number not in possible_numbers:
                    raise impossible_values_error.ImpossibleValuesError
                number = int(number)
                if number > pencils_num:
                    raise number_error.NumberError

                return number
            else:
                number = get_remove_num_bot(pencils_num)
                print_bot_move(number)

                return number

        except (impossible_values_error.ImpossibleValuesError, number_error.NumberError) as error:
            print_error(error)


def get_remove_num_bot(pencils_num: int) -> int:
    win_1 = []
    win_2 = []
    win_3 = []
    for num in range(2, pencils_num + 1, 4):
        win_1.append(num)
    for num in range(3, pencils_num + 1, 4):
        win_2.append(num)
    for num in range(4, pencils_num + 1, 4):
        win_3.append(num)

    if pencils_num in win_1:
        return 1
    if pencils_num in win_2:
        return 2
    if pencils_num in win_3:
        return 3

    while True:
        number = random.randint(1, 3)
        if number <= pencils_num:
            return number


def print_bot_move(pencils_num: int) -> None:
    print(pencils_num)


def print_error(error: Exception) -> None:
    print(error)


def print_winner(player: str) -> None:
    print('{} won!'.format(player))
