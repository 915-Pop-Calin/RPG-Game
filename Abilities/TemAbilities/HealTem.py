from Abilities.Ability import Ability


class HealTem(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        This has a small effect, as it heals the caster for 1. It's not a good ability though.
        """
        caster.heal(1)
        string = caster.get_name() + str( " heals for 1! \n")
        string += caster.get_name() + str(" is now at ") + str(caster.get_hp()) + " health! \n"
        return string
