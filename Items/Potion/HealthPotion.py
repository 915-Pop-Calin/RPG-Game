from Items.Potion.Potion import Potion


class HealthPotion(Potion):
    def __init__(self):
        super().__init__()
        self.__healing_value = 10

    def use(self, human_player):
        human_player.heal(self.__healing_value)

    def __str__(self):
        return "Health Potion: HEAL FOR " + str(self.__healing_value)

    def get_id(self):
        return 100
