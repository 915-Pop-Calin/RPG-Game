import random

from Abilities.Ability import Ability


class Focus(Ability):
    def __init__(self):
        super().__init__()
        self._description = "gain some of your sanity back\nuseful vs bosses that make you go insane\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        sanity_restored = random.randint(10, 40)
        caster.restore_sanity(sanity_restored)
        string = caster.get_name() + " has restored " + str(sanity_restored) + " of his sanity!\n"
        string += caster.get_name() + " is left with " + str(caster.get_sanity()) + " sanity!\n"
        return string