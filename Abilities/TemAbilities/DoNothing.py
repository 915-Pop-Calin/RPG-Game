from Abilities.Ability import Ability


class DoNothing(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        string = caster.get_name() + str( " does nothing! \n")
        string += "Seems pretty ineffective!\n"
        return string

