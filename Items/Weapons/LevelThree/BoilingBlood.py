from Items.Weapons.Weapon import Weapon


class BoilingBlood(Weapon):
    def __init__(self):
        super().__init__(40, 0)
        self.set_effect()
        self.set_life_steal(1.5)
        self._description = "VERY strong life stealer but deals you 40 damage every turn.\n"

    def effect(self, damage, caster, opponent):
        caster.deal_damage(caster, 40)
        string = "Boiling Blood has dealt 40 true damage to " + str(caster.get_name()) + str(" !\n")
        string += str(caster.get_name()) + " is left with " + str(caster.get_hp()) + str("health! \n")
        return string
