from Exceptions.exceptions import ShoppingError

from Items.Armors.Bandage import WornBandage
from Items.Armors.BootsOfDodge import BootsOfDodge
from Items.Armors.Cloth import Cloth
from Items.Armors.SteelPlateau import SteelPlateau
from Items.Armors.TemArmor import TemArmor
from Items.Potion.Potion import Potion
from Items.Potion.ExperiencePotion import ExperiencePotion
from Items.Potion.HealthPotion import HealthPotion
from Items.Weapons.BoilingBlood import BoilingBlood
from Items.Weapons.Eclipse import Eclipse
from Items.Weapons.IcarusesTouch import IcarusesTouch
from Items.Weapons.LanguageHacker import LanguageHacker
from Items.Weapons.TacosWhisper import TacosWhisper
from Items.Weapons.TankBuster import TankBuster
from Items.Weapons.ToyKnife import ToyKnife
from Items.Weapons.Words import Words


class Shop:
    def __init__(self, human_player, level):
        self._human_player = human_player
        self._level = level
        self._options = {2 : [[WornBandage(), 50], [Cloth(), 50], [Eclipse(), 100], [Words(), 50], [ToyKnife(), 50], [HealthPotion(), 10]],
                         3 : [[TemArmor(), 100], [SteelPlateau(), 100], [TacosWhisper(), 150], [LanguageHacker(), 200], [ExperiencePotion(), 1000]],
                         4 : [[BootsOfDodge(), 300], [BoilingBlood(), 400], [IcarusesTouch(), 400], [TankBuster(), 400]]}
        self._total_options = []
        for index in range (2, self._level + 1):
            for tuple in self._options[index]:
                self._total_options.append(tuple)

    def print_options(self):
        for option in self._total_options:
            print(type(option[0]).__name__, "cost:", option[1], "gold")

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
