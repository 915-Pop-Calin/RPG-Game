from Exceptions.exceptions import ShoppingError

from Items.Armors.Bandage import WornBandage
from Items.Armors.BootsOfDodge import BootsOfDodge
from Items.Armors.Cloth import Cloth
from Items.Armors.EyeOfSauron import EyeOfSauron
from Items.Armors.FireDeflector import FireDeflector
from Items.Armors.Scales import Scales
from Items.Armors.SteelPlateau import SteelPlateau
from Items.Armors.TemArmor import TemArmor
from Items.Armors.TidalArmour import TidalArmour
from Items.Potion.GrainOfSalt import GrainOfSalt
from Items.Potion.Potion import Potion
from Items.Potion.ExperiencePotion import ExperiencePotion
from Items.Potion.HealthPotion import HealthPotion
from Items.Weapons.BoilingBlood import BoilingBlood
from Items.Weapons.Eclipse import Eclipse
from Items.Weapons.IcarusesTouch import IcarusesTouch
from Items.Weapons.InfinityEdge import InfinityEdge
from Items.Weapons.LanguageHacker import LanguageHacker
from Items.Weapons.TacosWhisper import TacosWhisper
from Items.Weapons.TankBuster import TankBuster
from Items.Weapons.TheRing import TheRing
from Items.Weapons.TitansFindings import TitansFindings
from Items.Weapons.ToyKnife import ToyKnife
from Items.Weapons.Words import Words
from Items.Weapons.Xalatath import Xalatath


class Shop:
    def __init__(self, human_player, level):
        self._human_player = human_player
        self._level = level
        self._universal_option = [[HealthPotion(), 10], [ExperiencePotion(), 1000], [GrainOfSalt(), 50]]
        self._options = {2 : [[TemArmor(), 150], [Cloth(), 100], [Eclipse(), 150], [Words(), 50], [ToyKnife(), 50]],
                         3 : [ [SteelPlateau(), 400], [TacosWhisper(), 500], [TitansFindings(), 500]],
                         4 : [[BootsOfDodge(), 500], [BoilingBlood(), 500], [TankBuster(), 500], [LanguageHacker(), 600], [Xalatath(), 600]],
                         5 : [[Scales(), 200], [IcarusesTouch(), 900], [TidalArmour(), 700], [FireDeflector(), 800]],
                         6: [[EyeOfSauron(), 1000], [InfinityEdge(), 500]], 7: [[TheRing(), 1500]]}
        self._total_options = []
        for option in self._universal_option:
            self._total_options.append(option)
        if self._level > 1:
            for tuple in self._options[self._level]:
                self._total_options.append(tuple)

    def print_options(self):
        print(str(self._human_player.get_gold()) + " gold available")
        for option in self._total_options:
            print(option[0], "cost:", option[1], "gold\n")

    def search_item_by_name(self, name):
        for index in range (len(self._total_options)):
            if type(self._total_options[index][0]).__name__ == name:
                return index
        raise ShoppingError("Invalid Item To Buy!")

    def buy_item(self):
        self.print_options()
        choice = input("the item you want to buy:\n")
        index = self.search_item_by_name(choice)
        item = self._total_options[index]
        if not isinstance(item[0], Potion):
            self._total_options.remove(self._total_options[index])
        self._human_player.buy_item(item[1], item[0])
