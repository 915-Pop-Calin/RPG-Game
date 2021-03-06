from Abilities.Ability import Ability
from Exceptions.exceptions import CastingError


class Taunt(Ability):
    def __init__(self):
        super().__init__()
        self._description = "your opponent's attack and defense are decreased for 3 turns\nstacks with itself\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Opponent's attack and defense are decreased exponentially with relation to the level of the caster.
        If the attack or defense of the opponent would be reduced to 0 or below by this action, we raise a CastingError
        so it is not performed. To the list of actions to undo, we add the decast method of this ability.
        """
        difference = caster.get_level() ** 2
        if opponent.get_attack_value() <= difference or opponent.get_defense_value() <= difference:
            raise CastingError("Opponent's attack and defense cannot be reduced to 0!")
        opponent.decrease_attack_value(difference)
        opponent.decrease_defense_value(difference)
        string = "Your opponent's defense and attack were decreased by "
        string += str(difference)
        string += "!"
        if turn_counter + 3 in list_of_turns.keys():
            list_of_turns[turn_counter + 3].append(self.decast)
        else:
            list_of_turns[turn_counter + 3] = [self.decast]
        return string

    def decast(self, caster, opponent):
        """
        We set the attack and defense values of the opponent back to normal, because level cannot change mid-fight.
        """
        difference = caster.get_level() * 2
        opponent.increase_attack_value(difference)
        opponent.increase_defense_value(difference)
        string = "Your opponent's defense and attack were increased back by "
        string += str(difference)
        string += "!"
        return string