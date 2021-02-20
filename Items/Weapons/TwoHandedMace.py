from Exceptions.exceptions import StunError
from Items.Weapons.Weapon import Weapon


class TwoHandedMace(Weapon):
    def __init__(self):
        super().__init__(50, 0)
        self.set_passive()

    def passive(self, caster, opponent, list_of_turns, turn_counter):
        try:
            caster.stun()
            if turn_counter + 2 in list_of_turns.keys():
                list_of_turns[turn_counter + 2].append(self.decast)
            else:
                list_of_turns[turn_counter + 2] = [self.decast]
            string = caster.get_name() + " was stunned for a turn by TwoHandedMace!\n"
        except StunError as SE:
            string = str(SE)
        return string

    def decast(self, caster, opponent):
        caster.unstun()
        string = caster.get_name() + " can attack now!\n"
        return string

    def get_id(self):
        return 216