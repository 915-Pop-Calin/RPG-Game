from Abilities.CthulhuAbilities.MadnessCrit import MadnessCrit
from Abilities.CthulhuAbilities.TripleHit import TripleHit
from Characters.Character import Character
from Items.Armors.LevelFour.Scales import Scales
from Items.Weapons.Dreams import Dreams


class Cthulhu(Character):
    def __init__(self):
        super().__init__("Cthulhu", 7.5, 100, Dreams(), Scales(), 200, "The God which preys on your sanity\n")
        self.add_ability("triplehit", self.triplehit)
        self.add_ability("madnesscrit", self.madnesscrit)

    def triplehit(self, opponent, list_of_turns, turn_counter):
        ability = TripleHit()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def madnesscrit(self, opponent, list_of_turns, turn_counter):
        ability = MadnessCrit()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string


