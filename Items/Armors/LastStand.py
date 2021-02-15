from Items.Armors.Armour import Armour


class LastStand(Armour):
    def __init__(self):
        super().__init__(0, 400)
        self.set_passive()

    def passive(self, caster, opponent, list_of_turns, turn_counter):
        string = ""
        if caster.get_hp() / caster.get_max_hp() < 0.3:
            caster.decrease_defense_value(100)
            string = "Due to " + caster.get_name() + " being under 30% HP, his defense was reduced by 100 for a turn!\n"
            if turn_counter + 1 in list_of_turns.keys():
                list_of_turns[turn_counter + 1].append(self.decast)
            else:
                list_of_turns[turn_counter + 1] = [self.decast]
        return string

    def decast(self, caster, opponent):
        caster.increase_attack_value(100)
        string = caster.get_name() + "'s defenses were brought back to normal!\n"
        return string