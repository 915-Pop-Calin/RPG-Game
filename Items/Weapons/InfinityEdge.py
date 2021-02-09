from Items.Weapons.Weapon import Weapon


class InfinityEdge(Weapon):
    def __init__(self):
        super().__init__(20, 0)
        self._crit_chance = 0.35
