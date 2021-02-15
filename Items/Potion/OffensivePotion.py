from Items.Potion.Potion import Potion


class OffensePotion(Potion):
    def __init__(self):
        super().__init__()

    def use(self, human_player):
        original_defense = human_player.get_innate_defense()
        original_attack = human_player.get_innate_attack()
        human_player.set_innate_defense(original_defense - 20)
        human_player.set_innate_attack(original_attack + 20)
        string = "Your defense has been increased by 20, but your health was reduced by 5!\n"
        return string

    def __str__(self):
        return "OffensePotion: GAIN ATTACK BUT LOSE DEFENSE " + str(self._description)

    def get_id(self):
        return 107
