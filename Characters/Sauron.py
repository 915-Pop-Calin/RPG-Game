from Abilities.SauronAbilities.PowerOfTheEye import PowerOfTheEye
from Abilities.SauronAbilities.PowerOfTheRing import PowerOfTheRing
from Characters.Character import Character
from Items.Armors.EyeOfSauron import EyeOfSauron
from Items.Weapons.TheRing import TheRing


class Sauron(Character):
    def __init__(self):
        super().__init__("Sauron", 2, 200, TheRing(), EyeOfSauron(), 200, "The Creator of the Ring")
        self.add_ability("powerofthering", self.powerofthering)
        self.add_ability("poweroftheeye", self.poweroftheeye)

    def powerofthering(self, opponent, list_of_turns, turn_counter):
        ability = PowerOfTheRing()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def poweroftheeye(self, opponent, list_of_turns, turn_counter):
        ability = PowerOfTheEye()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string