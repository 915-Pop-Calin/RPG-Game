from Items.Potion.Potion import Potion


class GrainOfSalt(Potion):
    def __init__(self):
        super().__init__()
        self.__healing_per_level = 10
        self._description = "Scales with level.\n"

    def use(self, human_player):
        healing_done = self.__healing_per_level * human_player.get_level()
        human_player.heal(healing_done)
        string = "You have healed for " + str(healing_done) + " !\n"
        return string

    def __str__(self):
        return "GrainOfSalt: HEAL FOR " + str(self.__healing_per_level) + " PER LEVEL, " + self._description

    def get_id(self):
        return 102
