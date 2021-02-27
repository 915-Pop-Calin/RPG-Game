from Items.Weapons.Weapon import Weapon


class InfinityEdge(Weapon):
    def __init__(self):
        super().__init__(20, 0)
        self._crit_chance = 0.35
        self._description = "Increases your critical strike chance by 35%.\n"
