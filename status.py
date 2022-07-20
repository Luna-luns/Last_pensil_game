from player import Player


class Status:
    def __init__(self, player: Player):
        self.current_player = player

    def switch_status(self, player_1: Player, player_2: Player) -> None:
        if self.current_player == player_1:
            self.current_player = player_2
        else:
            self.current_player = player_1
