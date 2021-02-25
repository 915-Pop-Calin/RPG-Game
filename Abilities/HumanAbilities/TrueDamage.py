from Abilities.Ability import Ability


class TrueDamage(Ability):
    def __init__(self):
        super().__init__()
        self._description = "your armour penetration is set to 75% for 3 turns\nhas no effect if cast multiple times\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        caster.set_armour_pen(0.75)
        string = caster.get_name() + "'s armor penetration was set to 75%!\n"
        if turn_counter + 3 in list_of_turns.keys():
            list_of_turns[turn_counter + 3].append(self.decast)
        else:
            list_of_turns[turn_counter + 3] = [self.decast]
        return string

    def decast(self, caster, opponent):
        caster.set_defense_and_armour_to_normal()
        string = caster.get_name() + "'s armor penetration was brought back to normal!\n"
        return string