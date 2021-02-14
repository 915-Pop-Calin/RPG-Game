from Items.Weapons.Weapon import Weapon


class IcarusesTouch(Weapon):
    def __init__(self):
        super().__init__(0, 0)
        self.set_dot_effect([3, 5])
        self.set_effect()
        self._description = "Very strong DOTer.\n"

    def effect(self, damage, caster, opponent):
        opponent.add_dot_effect(self._dot_effect)
        return opponent.get_name() + " will take " + str(self._dot_effect[0]) + " damage every turn for " + str(self._dot_effect[1]) + " turns!\n"

    def get_id(self):
        return 206