from Items.Armors.Armour import Armour


class SaroniteScales(Armour):
    def __init__(self):
        super().__init__(0, 100)
        self._health = 100
        self._description = "Saronite Scales.\n"
        self._broken = False

    def take_hit(self, attack):
        multiplier = 100 / (100 + self.defense_value())
        damage = attack * multiplier
        self._health -= damage
        if self._health <= 0:
            self.set_defense(0)
            self._description = "Broken Saronite Scales.\n"
            self._broken = True
        string = "SaroniteScales have taken " + str(damage) + " damage!\n"
        string += "SaroniteScales are left with " + str(self._health) + " health!\n"
        return string

    def is_broken(self):
        return self._broken