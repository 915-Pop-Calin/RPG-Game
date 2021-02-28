from Abilities.Ability import Ability
import random

class Madness(Ability):
    def __init__(self):
        super().__init__()

    def cast(self, caster, opponent, list_of_turns, turn_counter):
        """
        The sanity of the opponent is permanently reduced by a random integer between 1 and 20 (on average, 10 insanity).
        """
        sanity_reducer = random.randint(1, 20)
        opponent.reduce_sanity(sanity_reducer)
        string = opponent.get_name() + "\b's sanity was reduced by " + str(sanity_reducer) + "!\n"
        string += opponent.get_name() + " has " + str(opponent.get_sanity()) + " sanity left!\n"
        return string