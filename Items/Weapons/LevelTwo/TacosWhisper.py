from Items.Weapons.Weapon import Weapon


class TacosWhisper(Weapon):
    def __init__(self):
        super().__init__(5, 0)
        self.set_effect()
        self.__turn_counter = 0
        self._description = "Each fourth shot strikes thrice.\n"

    def effect(self, damage, caster, opponent):
        print("turn:", self.__turn_counter)
        if self.__turn_counter == 3:
            caster.deal_damage(opponent, 2 * damage)
            self.__turn_counter = 0
            string = "Taco's whisper has dealt " + str(2 * damage) + " with the fourth shot!\n"
        else:
            self.__turn_counter += 1
            string = ""
        return string
