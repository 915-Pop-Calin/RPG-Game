from Items.Potion.Potion import Potion


class GrainOfSalt(Potion):
    def __init__(self):
        super().__init__()
        self.__healing_per_level = 10

    def use(self, human_player):
        human_player.heal(self.__healing_per_level * human_player.get_level())
        string = "You have healed for " + str(self.__healing_per_level) + " !\n"
        return string

    def __str__(self):
        return "GrainOfSalt: HEAL FOR " + str(self.__healing_per_level) + " PER LEVEL"

    def get_id(self):
        return 102
