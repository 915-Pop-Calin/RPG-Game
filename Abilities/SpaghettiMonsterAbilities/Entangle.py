from Abilities.Ability import Ability


class Entangle(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Opponent is stalled for one turn by being stun, and the undo of this action is added to the list of abilities
        to undo.
        """
        opponent.stun()
        string = caster.get_name() + " casts Entangle!\n"
        string += opponent.get_name() + " is stunned for one turn!\n"
        if turn_counter + 1 in list_of_turns.keys():
            list_of_turns[turn_counter + 1].append(self.decast)
        else:
            list_of_turns[turn_counter + 1] = [self.decast]
        return string

    def decast(self, caster, opponent):
        """
        Caster is unstunned and he can do stuff again.
        """
        opponent.unstun()
        string = opponent.get_name() + " is no longer stunned!\n"
        return string