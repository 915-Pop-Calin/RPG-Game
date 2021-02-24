from Abilities.Ability import Ability


class Discourage(Ability):
    def __init__(self):
        super().__init__()
        self._description = "enemy's attack value is reduced to 0 for a turn\nmay be useful against some unkillable bosses\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        opponent.set_attack_value(0)
        string = opponent.get_name() + "'s attack value was decreased to 0!\n"
        if turn_counter + 1 in list_of_turns.keys():
            list_of_turns[turn_counter + 1].append(self.decast)
        else:
            list_of_turns[turn_counter + 1] = [self.decast]
        return string

    def decast(self, caster, opponent):
        opponent.set_defense_and_armour_to_normal()
        string = opponent.get_name() + "'s attack was brought back to normal!\n"
        return string
