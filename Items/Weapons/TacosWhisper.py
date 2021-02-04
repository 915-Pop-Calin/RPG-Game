from Items.Weapons.Weapon import Weapon


class TacosWhisper(Weapon):
    def __init__(self):
        super().__init__(5, 0)
        self.set_effect()
        self.__turn_counter = 0

    def effect(self, damage, caster, opponent):
        if self.__turn_counter == 4:
            caster.deal_damage(opponent, damage)
            self.__turn_counter = 0
            string = "Taco's whisper has dealt " + str(damage) + " with the fourth shot!\n"
        else:
            self.__turn_counter += 1
            string = None
        return string

    def get_id(self):
        return 203