from Abilities.Ability import Ability


class Bolster(Ability):
    def __init__(self):
        super().__init__()
        #self._

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        difference = caster.get_level() * 2
        opponent.decrease_attack_value(difference)
        caster.increase_attack_value(difference)
        string = "Your attack was increased by "
        string += str(difference)
        string += "!"
        list_of_turns[turn_counter + 3] = self.decast
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

