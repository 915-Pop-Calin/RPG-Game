from Abilities.Ability import Ability


class Strengthen(Ability):
    def __init__(self):
        super().__init__()
        self._description = "your attack and defense are increased for 3 turns\nstacks with itself\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Caster's attack and defense are increased exponentially with relation to the level of the caster, and to the list
        of abilities to undo, the decast method is added.
        """
        difference = caster.get_level() ** 2
        caster.increase_attack_value(difference)
        caster.increase_defense_value(difference)
        string = "Your attack value and defense were increased by "
        string += str(difference)
        string += "!"
        if turn_counter + 3 in list_of_turns.keys():
            list_of_turns[turn_counter + 3].append(self.decast)
        else:
            list_of_turns[turn_counter + 3] = [self.decast]
        return string

    def decast(self, caster, opponent):
        """
        Everything is set back to normal. Works normally because level cannot change mid-fight, or at least should not.
        """
        difference = caster.get_level() * 2
        caster.decrease_attack_value(difference)
        caster.decrease_defense_value(difference)
        string = "Your attack value and defense were decreased back by "
        string += str(difference)
        string += "!"
        return string
