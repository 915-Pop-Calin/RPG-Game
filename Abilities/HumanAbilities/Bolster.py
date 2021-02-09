from Abilities.Ability import Ability
from Exceptions.exceptions import CastingError


class Bolster(Ability):
    def __init__(self):
        super().__init__()
        self._description = "your attack is increased while your opponent's attack is decreased for 3 turns\nstacks with itself\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        difference = caster.get_level() * 2
        if opponent.get_attack_value() <= caster.get_level() * 2:
            raise CastingError("Opponent's attack cannot be reduced to 0!")
        opponent.decrease_attack_value(difference)
        caster.increase_attack_value(difference)
        string = "Your attack was increased by "
        string += str(difference)
        string += "!"
        if turn_counter + 3 in list_of_turns.keys():
            list_of_turns[turn_counter + 3].append(self.decast)
        else:
            list_of_turns[turn_counter + 3] = [self.decast]
        return string

    def decast(self, caster, opponent):
        difference = caster.get_level() * 2
        opponent.increase_attack_value(difference)
        caster.decrease_attack_value(difference)
        string = "Your attack was decreased back by "
        string += str(difference)
        string += " and your opponent's attack was increased back by "
        string += str(difference)
        string += "!"
        return string

