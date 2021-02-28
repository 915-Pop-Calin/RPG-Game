from Abilities.Ability import Ability


class TripleHit(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        The caster halves its attack and it hits three times (equal to 1.5 attacks at normal attack), but it triggers
        on-hit effects three times. Afterwards, its attack is brought to normal.
        """
        string = caster.get_name() + " has casted TripleHit!\n"
        attack = caster.get_attack_value()
        caster.set_attack_value(0.5 * attack)
        string += caster.hit(opponent, list_of_turns, turn_counter)
        string += caster.hit(opponent, list_of_turns, turn_counter)
        string += caster.hit(opponent, list_of_turns, turn_counter)
        caster.set_attack_value(attack)
        return string

