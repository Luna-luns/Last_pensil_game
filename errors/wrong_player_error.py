class WrongPlayerError(Exception):
    def __init__(self, name_1: str, name_2: str):
        self.message = "Choose between '{}' and '{}'".format(name_1, name_2)
        super().__init__(self.message)
