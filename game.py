from player import Player
import user_interface
from status import Status


player_1 = Player('John')
player_2 = Player('Jack')

pencils_number = user_interface.ask_pencils_num()
first_player = user_interface.ask_first_player(player_1, player_2)
status = Status(first_player)

while True:
    user_interface.print_pencils(pencils_number)
    pencils_to_remove = user_interface.ask_remove_num(status.current_player.name, pencils_number)
    pencils_number -= pencils_to_remove
    status.switch_status(player_1, player_2)

    if pencils_number <= 0:
        user_interface.print_winner(status.current_player.name)
        break
