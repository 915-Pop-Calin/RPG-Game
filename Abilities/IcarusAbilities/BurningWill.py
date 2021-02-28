from Abilities.Ability import Ability


class BurningWill(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Three DOT effects are added to the opponent which will deal 7 true damage at the beginning of each turn
        (so, in total 21 true damage at the beginning of each turn) for 3 turns.
        """
        dot_effects = [[7, 3], [7, 3], [7, 3]]
        for dot_effect in dot_effects:
            opponent.add_dot_effect(dot_effect)
        string = caster.get_name() + " has cast BurningWill!\n"
        string += opponent.get_name() + " will take 7 damage every turn for 3 turns THRICE!\n"
        return string