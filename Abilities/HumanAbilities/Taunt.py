from Abilities.Ability import Ability


class Taunt(Ability):
    def __init__(self):
        super().__init__()
        self.__turns = 2


    def cast(self, caster, opponent, list_of_turns, turn_counter):
        difference = caster.get_level() * 2
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
        difference = caster.get_level() * 2
        opponent.increase_attack_value(difference)
        opponent.increase_defense_value(difference)
        string = "Your opponent's defense and attack were increased back by "
        string += str(difference)
        string += "!"
        return string