import random

from Items.Armors.Armour import Armour


class FireDeflector(Armour):
    def __init__(self):
        super().__init__(0, 75)
        self.set_effect()

    def effect(self, damage, caster, opponent):
        random_choice = random.randint(1,4)
        string = ""
        if random_choice == 1:
            dot_effects = caster.get_dot_effects()
            for dot_effect in dot_effects:
                opponent.add_dot_effect(dot_effect)
            caster.clear_dot_effects()
            string = caster.get_name() + " has deflected his DOT effects onto " + opponent.get_name() + "!\n"
        return string

    def get_id(self):
        return 308