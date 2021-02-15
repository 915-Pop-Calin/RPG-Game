from Abilities.IcarusAbilities.Burn import Burn
from Abilities.IcarusAbilities.BurningWill import BurningWill
from Characters.Character import Character
from Items.Armors.LevelTwo.SteelPlateau import SteelPlateau
from Items.Weapons.LevelFour.IcarusesTouch import IcarusesTouch


class Icarus(Character):
    def __init__(self):
        super().__init__("Icarus", 0, 100, IcarusesTouch(), SteelPlateau(), 200, "The corrupted mythological figure by flying too close to the sun")
        self.add_ability("burn", self.burn)
        self.add_ability("burningwill", self.burning_will)

    def burn(self, opponent, list_of_turns, turn_counter):
        ability = Burn()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def burning_will(self, opponent, list_of_turns, turn_counter):
        ability = BurningWill()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string