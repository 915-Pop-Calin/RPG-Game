from Items.Potion.Potion import Potion


class DefensePotion(Potion):
    def __init__(self):
        super().__init__()
        self._description = "Increase defense points at the cost of health.\n"

    def use(self, human_player):
        original_defense = human_player.get_innate_defense()
        human_player.set_innate_defense(original_defense + 20)
        human_player.permanently_reduce_hp(5)
        string = "Your defense has been increased by 20, but your health was reduced by 5!\n"
        return string
