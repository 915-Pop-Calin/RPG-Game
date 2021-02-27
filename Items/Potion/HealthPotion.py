from Items.Potion.Potion import Potion


class HealthPotion(Potion):
    def __init__(self):
        super().__init__()
        self.__healing_value = 10
        self._description = "Flat heal for 10.\n"

    def use(self, human_player):
        human_player.heal(self.__healing_value)
        string = "You have healed for " + str(self.__healing_value) + " !\n"
        return string
