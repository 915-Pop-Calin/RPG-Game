from Abilities.Ability import Ability


class PowerOfTheRing(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        attack = caster.get_attack_value()
        defense = caster.get_defense_value()
        caster.set_attack_value(attack * 5)
        caster.set_defense_value(defense * 5)
        string = caster.get_name() + "'s defense and attack were multiplied by 5!\n"
        string += caster.get_name() + " now has " + str(attack) + " attack and " + str(defense) + " defense!\n"
        if turn_counter + 3 in list_of_turns.keys():
            list_of_turns[turn_counter + 3].append(self.decast)
        else:
            list_of_turns[turn_counter + 3] = [self.decast]
        return string

    def decast(self, caster, opponent):
        caster.set_defense_and_armour_to_normal()
        string = caster.get_name() + "'s defense and attack were brought back to normal!\n"
        return string