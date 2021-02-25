from Items.Weapons.Weapon import Weapon


class DoubleEdgedSword(Weapon):
    def __init__(self):
        super().__init__(20, 0)
        self.set_passive()
        self._description = "Huge Attack Weapon, but your opponent's attacks are stronger.\n"

    def passive(self, caster, opponent, list_of_turns, turn_counter):
        opponent.increase_attack_value(10)
        if turn_counter + 2 in list_of_turns.keys():
            list_of_turns[turn_counter + 2].append(self.decast)
        else:
            list_of_turns[turn_counter + 2] = [self.decast]
        string = opponent.get_name() + "'s attack was increased by 10 for a turn by DoubleEdgedSword!\n"
        return string

    def decast(self, caster, opponent):
        opponent.decrease_attack_value(10)
        string = opponent.get_name() + "'s attack was decreased back by 10 for a turn by DoubleEdgedSword!\n"
        return string

    def get_id(self):
        return 214