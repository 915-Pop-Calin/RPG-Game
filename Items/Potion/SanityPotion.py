from Items.Potion.Potion import Potion


class SanityPotion(Potion):
    def __init__(self):
        super().__init__()
        self._sanity_restoring_value = 30
        self._description = "Restore 30 of your sanity.\n"

    def use(self, human_player):
        human_player.restore_sanity(self._sanity_restoring_value)
        string = "You have restored " + str(self._sanity_restoring_value) + " of your sanity!\n"
        return string

    def get_id(self):
        return 103