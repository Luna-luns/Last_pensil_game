from player import Player
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


def ask_remove_num(name: str, pencils_num: int) -> int:
    possible_numbers = {'1', '2', '3'}
    print("{}'s turn!".format(name))
    while True:
        try:
            number = input()
            if number not in possible_numbers:
                raise impossible_values_error.ImpossibleValuesError
            number = int(number)
            if number > pencils_num:
                raise number_error.NumberError
            return number
        except (impossible_values_error.ImpossibleValuesError, number_error.NumberError) as error:
            print_error(error)


def print_error(error: Exception) -> None:
    print(error)


def print_winner(player: str) -> None:
    print('{} won!'.format(player))
