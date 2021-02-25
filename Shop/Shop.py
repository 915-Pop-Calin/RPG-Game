from Exceptions.exceptions import ShoppingError
from Items.Armors.LastStand import LastStand
from Items.Armors.LevelFive.EyeOfSauron import EyeOfSauron
from Items.Armors.LevelFour.FireDeflector import FireDeflector
from Items.Armors.LevelFour.Scales import Scales
from Items.Armors.LevelFour.TidalArmour import TidalArmour
from Items.Armors.LevelOne.Bandage import WornBandage
from Items.Armors.LevelOne.Cloth import Cloth
from Items.Armors.LevelOne.TemArmor import TemArmor
from Items.Armors.LevelThree.BootsOfDodge import BootsOfDodge
from Items.Armors.LevelTwo.SteelPlateau import SteelPlateau
from Items.Armors.NinjaYoroi import NinjaYoroi
from Items.Potion.DefensePotion import DefensePotion
from Items.Potion.GrainOfSalt import GrainOfSalt
from Items.Potion.HealthPotion import HealthPotion
from Items.Potion.OffensePotion import OffensePotion
from Items.Potion.Potion import Potion
from Items.Weapons.DoubleEdgedSword import DoubleEdgedSword
from Items.Weapons.Dreams import Dreams
from Items.Weapons.GiantSlayer import GiantSlayer
from Items.Weapons.LevelFive.InfinityEdge import InfinityEdge
from Items.Weapons.LevelFive.RadusBiceps import RadusBiceps
from Items.Weapons.LevelFour.IcarusesTouch import IcarusesTouch
from Items.Weapons.LevelOne.Eclipse import Eclipse
from Items.Weapons.LevelOne.ToyKnife import ToyKnife
from Items.Weapons.LevelOne.Words import Words
from Items.Weapons.LevelSix.TheRing import TheRing
from Items.Weapons.LevelThree.BoilingBlood import BoilingBlood
from Items.Weapons.LevelThree.LanguageHacker import LanguageHacker
from Items.Weapons.LevelThree.TankBuster import TankBuster
from Items.Weapons.LevelThree.Xalatath import Xalatath
from Items.Weapons.LevelTwo.TacosWhisper import TacosWhisper
from Items.Weapons.LevelTwo.TitansFindings import TitansFindings
from Items.Weapons.TwoHandedMace import TwoHandedMace


class Shop:
    def __init__(self, human_player, level):
        self._human_player = human_player
        self._level = level
        self._universal_option = [[HealthPotion(), 10], [GrainOfSalt(), 50], [DefensePotion(), 100], [OffensePotion(), 100]]
        self._options = {2 : [[TemArmor(), 150], [Cloth(), 100], [Eclipse(), 150], [Words(), 50], [ToyKnife(), 50], [WornBandage(), 0], [TwoHandedMace(), 200]],
                         3 : [ [SteelPlateau(), 400], [TacosWhisper(), 500], [TitansFindings(), 500], [DoubleEdgedSword(), 400]],
                         4 : [[BootsOfDodge(), 500], [BoilingBlood(), 500], [TankBuster(), 500], [LanguageHacker(), 600], [Xalatath(), 600], [LastStand(), 600]],
                         5 : [[Scales(), 200], [IcarusesTouch(), 900], [TidalArmour(), 700], [FireDeflector(), 800], [GiantSlayer(), 900]],
                         6: [[EyeOfSauron(), 1000], [InfinityEdge(), 500], [RadusBiceps(), 700], [NinjaYoroi(), 1000]],
                         7: [[TheRing(), 1500], [Dreams(), 400]]}
        self._total_options = []
        for option in self._universal_option:
            self._total_options.append(option)
        '''if self._level > 1:
            for tuple in self._options[self._level]:
                self._total_options.append(tuple)'''
        for index in range (2, self._level + 1):
            for tuple in self._options[index]:
                self._total_options.append(tuple)
        self._all_items = []
        for index in range (2, 8):
            for tuple in self._options[index]:
                self._all_items.append(tuple)


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
        '''if not isinstance(item[0], Potion):
            self._total_options.remove(self._total_options[index])'''
        self._human_player.buy_item(item[1], item[0])

    def find_cost_by_class(self, class_name):
        for option in self._all_items:
            if type(option[0]).__name__.lower().strip() == type(class_name).__name__.lower().strip():
                return option[1]
        return None

    def sell_item(self):
        for element in self._human_player.get_inventory():
            if element is not None:
                print(element, " GOLD: ", 0.75 * self.find_cost_by_class(element), "\n")
        choice = input("the item you want to sell:\n")
        choice = choice.lower().strip()
        for option in self._all_items:
            if type(option[0]).__name__.lower() == choice:
                self._human_player.sell_item(0.75 * option[1], choice)
                return True
        raise ShoppingError("Item Cannot Be Found In Shop!\n")