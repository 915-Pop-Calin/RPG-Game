from Abilities.Ability import Ability


class Burn(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Depending on what turn it is, defined by the integer number turn_counter, a new dot effect is created to be cast
        on the opponent: the opponent will take as much true damage as the turn counter for 5 turns.
        """
        dot_effect = [turn_counter, 5]
        opponent.add_dot_effect(dot_effect)
        string = caster.get_name() + " has cast burn!\n"
        string += opponent.get_name() + " will take " + str(dot_effect[0]) + " damage every turn for " + str(dot_effect[1]) + " turns!\n"
        return string