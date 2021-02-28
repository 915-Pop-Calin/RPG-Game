from Abilities.Ability import Ability


class CCImunity(Ability):
    def __init__(self):
        super().__init__()
        self._description = "you become immune to CC for 5 turns\n"

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        The caster becomes immune to stuns for 5 turns, meaning that he cannot be stunned by anything.
        We add the decast of this class to the list of abilities to undo, in order for it to last only 5 turns.
        """
        caster.set_stun_resistant(True)
        string = caster.get_name() + " is immune to stuns for 5 turns!\n"
        if turn_counter + 5 in list_of_turns.keys():
            list_of_turns[turn_counter + 5].append(self.decast)
        else:
            list_of_turns[turn_counter + 5] = [self.decast]
        return string

    def decast(self, caster, opponent):
        """
        We decast the ability and make the caster prone to CC back again, meaning that he can be stunned now.
        """
        caster.set_stun_resistant(False)
        string = caster.get_name() + " is no longer immune to stuns!\n"
        return string