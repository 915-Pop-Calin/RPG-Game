from Abilities.Ability import Ability


class MadnessCrit(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        missing_sanity = 100 - opponent.get_sanity()
        percentage_missing = missing_sanity / 100
        percentage_missing = round(percentage_missing, 2)
        enhancer = 1 + 2 * percentage_missing
        attack_value = caster.get_attack_value()
        string = opponent.get_name() + " has taken " + str(attack_value * enhancer) + " True Damage due to its missing sanity!\n"
        string += opponent.get_name() + " is left with " + str(opponent.get_hp()) + " health!\n"
        opponent.reduce_hp(attack_value * enhancer)
        return string