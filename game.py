def ask_pencils_num() -> int:
    return int(input('How many pencils would you like to use:').strip())


def ask_first_player(name_1: str, name_2: str) -> str:
    return input('Who will be the first ({}, {}):'.format(name_1, name_2)).strip()


def print_pencils(num: int) -> None:
    print('|' * num)


def print_first_player(name: str) -> None:
    print('{} is going first!'.format(name))


name1 = 'John'
name2 = 'Jack'
pencils_number = ask_pencils_num()
first_player = ask_first_player(name1, name2)
print_pencils(pencils_number)
print_first_player(first_player)
