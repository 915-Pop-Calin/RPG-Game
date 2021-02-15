from Items.Weapons.Weapon import Weapon

class SaroniteTentacles(Weapon):
    def __init__(self):
        super().__init__(20, 0)
        self._health = 100
        self.__broken = False
        self.set_reflector()

    def take_hit(self, damage):
        self._health -= damage
        if self._health <= 0:
            self.set_attack(0)
            self._description = "Broken Saronite Scales.\n"

            self.__broken = True
        string = "SaroniteScales have taken " + str(damage) + " damage!\n"
        string += "SaroniteScales are left with " + str(self._health) + " health!\n"
        return string

    def is_broken(self):
        return self.__broken

    def get_health(self):
        return self._health