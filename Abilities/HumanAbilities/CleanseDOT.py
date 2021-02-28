from Abilities.Ability import Ability


class CleanseDOT(Ability):
    def __init__(self):
        super().__init__()
        self._description = "caster clears all the dot effects that affect him\nmay be useful vs bosses that burn you\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        The caster is cleansed of all DOT effects on him. It needs no decasting because it is a one-time thing.
        """
        caster.clear_dot_effects()
        string = caster.get_name() + " cleared all his DOT effects!\n"
        return string
