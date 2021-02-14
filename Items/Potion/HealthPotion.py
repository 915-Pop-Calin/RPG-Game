from Items.Potion.Potion import Potion


class HealthPotion(Potion):
    def __init__(self):
        super().__init__()
        self.__healing_value = 10
        self._description = "Flat heal.\n"

    def use(self, human_player):
        human_player.heal(self.__healing_value)
        string = "You have healed for " + str(self.__healing_value) + " !\n"
        return string

    def __str__(self):
        return "HealthPotion: HEAL FOR " + str(self.__healing_value) + ", " + str(self._description)

    def get_id(self):
        return 100
