from Abilities.Ability import Ability


class PowerOfTheEye(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Opponent's sanity is reduced by a flat 50, meaning that any 2 of these abilities will kill the player if
        he takes no defensive action.
        """
        opponent.reduce_sanity(50)
        string = opponent.get_name() + " stares into the Eye of Sauron!\n"
        string += opponent.get_name() + "'s sanity is reduced by 50!\n"
        return string
