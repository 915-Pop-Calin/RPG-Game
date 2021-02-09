from Abilities.Ability import Ability


class TripleHit(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        string = caster.get_name() + " has casted TripleHit!\n"
        string += caster.hit(opponent, list_of_turns, turn_counter)
        string += caster.hit(opponent, list_of_turns, turn_counter)
        string += caster.hit(opponent, list_of_turns, turn_counter)
        return string

