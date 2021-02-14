import math


class Cheats:
    def __init__(self):
        self.list_of_cheats = {"mpcezarrus": self.god_mode, "mpearlybird": self.level_2, "mpmadness": self.level_3,
                               "mpinsanity": self.level_4, "mpaugust": self.level_5, "mpmyprecious": self.level_6, "mpneltharion": self.level_7,
                               "mpgreedisgood": self.infinite_gold}

    def god_mode(self, game):
        game.get_player().set_innate_attack(math.inf)
        game.get_player().set_innate_defense(math.inf)
        game.get_player().set_innate_health(math.inf)
        game.set_cheats()
        string = "God mode has been activated!\n"
        return string

    def level_2(self, game):
        game.set_level(2)
        game.set_cheats()
        game.get_player().cheat_to_level(2)
        string = "You have jumped to level 2!\n"
        return string

    def level_3(self, game):
        game.set_level(3)
        game.set_cheats()
        game.get_player().cheat_to_level(3)
        string = "You have jumped to level 3!\n"
        return string

    def level_4(self, game):
        game.set_level(4)
        game.set_cheats()
        game.get_player().cheat_to_level(4)
        string = "You have jumped to level 4!\n"
        return string

    def level_5(self, game):
        game.set_level(5)
        game.set_cheats()
        game.get_player().cheat_to_level(5)
        string = "You have jumped to level 5!\n"
        return string

    def level_6(self, game):
        game.set_level(6)
        game.set_cheats()
        game.get_player().cheat_to_level(6)
        string = "You have jumped to level 6!\n"
        return string

    def level_7(self, game):
        game.set_level(7)
        game.set_cheats()
        game.get_player().cheat_to_level(7)
        string = "You have jumped to level 7!\n"
        return string

    def infinite_gold(self, game):
        game.get_player().gain_gold(math.inf)
        game.set_cheats()
        string = "You have gained infinite gold!\n"
        return string

