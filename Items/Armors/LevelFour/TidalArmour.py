from Items.Armors.Armour import Armour


class TidalArmour(Armour):
    def __init__(self):
        super().__init__(0, 30)
        self.set_effect()
        self._description = "Helps you put out fire.\n"

    def effect(self, damage, caster, opponent):
        caster.decrease_dot_effects(1)
        string = caster.get_name() + " has decreased all dot effects on him by 1!\n"
        return string
