from Abilities.Ability import Ability


class BlindingRage(Ability):
    def __init__(self):
        super().__init__()
        self._description = "your attack doubles while your defense is halved for 3 turns\ndoes not stack with itself\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        print(caster.get_attack_value())
        print(caster.get_armour())
        caster.set_attack_value(caster.get_attack_value() * 2)
        caster.set_defense_value(caster.get_armour() * 2)
        print(caster.get_attack_value())
        print(caster.get_armour())
        string = "In a blinding rage, your attack value was doubled and your defense value was halved!"
        if turn_counter + 3 in list_of_turns.keys():
            list_of_turns[turn_counter + 3].append(self.decast)
        else:
            list_of_turns[turn_counter + 3] = [self.decast]
        return string

    def decast(self, caster, opponent):
        caster.set_defense_and_armour_to_normal()
        string = "Your attack value and your defense were brought back to normal!"
        return string