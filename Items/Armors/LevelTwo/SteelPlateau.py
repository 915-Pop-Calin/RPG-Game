from Items.Armors.Armour import Armour


class SteelPlateau(Armour):
    def __init__(self):
        super().__init__(0, 200)
        self.set_effect()
        self._description = "Very strong armor but deals damage to you every turn. Allows you to go below 0 HP for a short period.\n"

    def effect(self, damage, caster, opponent):
        caster.deal_damage(caster, 5)
        string = "Steel Plateau has dealt 5 true damage to " + str(caster.get_name()) + str("! \n")
        string += str(caster.get_name()) + " is left with " + str(caster.get_hp()) + str("health! \n")
        return string
