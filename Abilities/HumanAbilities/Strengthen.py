from Abilities.Ability import Ability


class Strengthen(Ability):
    def __init__(self):
        super().__init__()
        self.__turns = 2

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        difference = caster.get_level() * 2
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
        difference = caster.get_level() * 2
        caster.decrease_attack_value(difference)
        caster.decrease_defense_value(difference)
        string = "Your attack value and defense were decreased back by "
        string += str(difference)
        string += "!"
        return string
