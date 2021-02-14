from Items.Potion.Potion import Potion


class ExperiencePotion(Potion):
    def __init__(self):
        super().__init__()
        self.__level = 1
        self._description = "Helps you get abilities quicker.\n"

    def use(self, human_player):
        human_player.level_up()
        string = "You leveled up to level " + str(human_player.get_level()) + " !\n"
        return string

    def __str__(self):
        return "ExperiencePotion: LEVEL UP INSTANTLY, " + self._description

    def get_id(self):
        return 101