from Items.Potion.Potion import Potion


class SanityPotion(Potion):
    def __init__(self):
        super().__init__()
        self._sanity_restoring_value = 30
        self._description = "Makes you go sane\n"

    def use(self, human_player):
        human_player.restore_sanity(self._sanity_restoring_value)
        string = "You have restored " + str(self._sanity_restoring_value) + " of your sanity!\n"
        return string

    def __str__(self):
        string = "SanityPotion: RESTORE " + str(self._sanity_restoring_value) + " OF YOUR SANITY, " + self._description
        return string

    def get_id(self):
        return 103