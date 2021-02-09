import math


class Cheats:
    def __init__(self):
        self.list_of_cheats = {"mpcezarrus": self.god_mode, "mpearlybird": self.level_2, "mpmadness": self.level_3,
                               "mpinsanity": self.level_4, "mpgreedisgood": self.infinite_gold}

    def god_mode(self, game):
        game.get_player().set_attack_value(math.inf)
        game.get_player().set_defense_value(math.inf)
        game.get_player().set_hp(math.inf)
        game.set_cheats()

    def level_2(self, game):
        game.set_level(2)
        game.set_cheats()

    def level_3(self, game):
        game.set_level(3)
        game.set_cheats()

    def level_4(self, game):
        game.set_level(4)
        game.set_cheats()

    def infinite_gold(self, game):
        game.get_player().gain_gold(math.inf)
        game.set_cheats()

