from player import Player


def ask_pencils_num() -> int:
    return int(input('How many pencils would you like to use:' + '\n').strip())


def ask_first_player(player_1: Player, player_2: Player) -> Player:
    name = input('Who will be the first ({}, {}):\n'.format(player_1, player_2)).strip()
    if player_1.name == name:
        return player_1

    return player_2


def print_pencils(num: int) -> None:
    print('|' * num)


def ask_remove_num(name: str) -> int:
    return int(input("{}'s turn:\n".format(name)))


# def print_first_player(name: str) -> None:
#    print('{} is going first!'.format(name))
