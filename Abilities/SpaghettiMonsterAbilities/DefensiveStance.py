from Abilities.Ability import Ability


class DefensiveStance(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        Caster goes into a defensive stance for 2 turns, having 100 defense but its attack reduced to 0. The decast is
        added to the list of abilities to undo.
        """
        caster.set_attack_value(1)
        caster.increase_defense_value(100)
        string = caster.get_name() + " enters into a defensive stance!\n"
        string += caster.get_name() + " gains 100 defense, but his attack is reduced to 1!\n"
        if turn_counter + 2 in list_of_turns.keys():
            list_of_turns[turn_counter + 2].append(self.decast)
        else:
            list_of_turns[turn_counter + 2] = [self.decast]
        return string

    def decast(self, caster, opponent):
        """
        Everything is set back to normal, so all debuffs are removed through this.
        """
        caster.set_defense_and_armour_to_normal()
        string = caster.get_name() + "\b's defense and attack were brought back to normal!\n"
        return string

