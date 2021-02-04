from Items.Potion.Potion import Potion


class ExperiencePotion(Potion):
    def __init__(self):
        super().__init__()
        self.__level = 1

    def use(self, human_player):
        human_player.level_up()

    def __str__(self):
        return "Experience Potion: LEVEL UP INSTANTLY"

    def get_id(self):
        return 101