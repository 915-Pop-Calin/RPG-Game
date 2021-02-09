import random

from Characters.Cthulhu import Cthulhu
from Characters.HumanPlayer import HumanPlayer
from Characters.SpaghettiMonster import SpaghettiMonster
from Characters.Tem import Tem
from Characters.YoggSaron import YoggSaron
from Cheats.Cheats import Cheats
from Combat.Combat import Combat
from Exceptions.exceptions import ShoppingError, ItemError, PickingError
from Items.Potion.ExperiencePotion import ExperiencePotion
from Items.Potion.HealthPotion import HealthPotion
from Items.Potion.SanityPotion import SanityPotion
from Shop.Shop import Shop


class Game:
    def __init__(self):
        self.__player = None
        self.__dead = False
        self.__enemy = None
        self.__combat = None
        self.__in_combat = True
        self.__save_file = "saved.txt"
        self.__exit = False
        self.__level = 1
        self.droppable_items = []
        self.level_specific_enemy ={1: Tem, 2: SpaghettiMonster, 3: YoggSaron, 4: Cthulhu}
        self.level_specific_consumable = {2: [HealthPotion, 3], 3: [ExperiencePotion, 1], 4: [SanityPotion, 2]}
        self.__shop = Shop(self.__player, self.__level)
        self.__hasCheated = False
        self.__cheats = Cheats()

    def initialise_game(self):
        decision = input("Do you want to load your save file? Y/N\n")
        if decision.upper().strip() == "Y":
            self.__player = HumanPlayer("filler")
            self.load()
        else:
            name = input("The name you want to use from now on is:\n")
            human = HumanPlayer(name)
            self.__player = human
        self.out_of_combat()

    def out_of_combat(self):
        decision = None
        while decision != "next":
            decision = input("next\nstats\nequip item\nsave\nsee abilities\nshop\nexit\n")
            decision = decision.lower().strip()
            if decision == "stats":
                print(self.__player.print_stats())
            elif decision == "equip item":
                try:
                    print(self.__player.print_inventory())
                    item = input("the item you want to equip:\n")
                    string = self.__player.use_item(item)
                    print(string)
                except ItemError as IE:
                    print(str(IE))
            elif decision == "save":
                if self.__cheats:
                    print("Game cannot be saved because you cheated!\n")
                else:
                    self.save()
            elif decision == "exit":
                self.__exit = True
                break
            elif decision == "see abilities":
                self.__player.print_abilities_description()
            elif decision == "shop":
                try:
                    self.__shop.buy_item()
                except ShoppingError as PE:
                    print(str(PE))
                except PickingError as PE:
                    print(str(PE))
            elif decision in self.__cheats.list_of_cheats.keys():
                self.__cheats.list_of_cheats[decision](self)
            elif decision != "next":
                print("Invalid Command!")

    def level(self):
        self.__enemy = self.level_specific_enemy[self.__level]()
        string = "WILD "
        string += type(self.__enemy).__name__.upper()
        string += " APPEARED!"
        print(string)
        self.combat()

    def combat(self):
        combat = Combat(self.__player, self.__enemy)
        self.__combat = combat
        self.__combat.fight()
        if self.__combat.isDead():
            self.__dead = True

    def drops(self):
        self.droppable_items.append(self.__enemy.get_weapon())
        self.droppable_items.append(self.__enemy.get_armor())

    def post_combat_drops(self):
        self.__shop = Shop(self.__player, self.__level)
        self.drops()
        index = random.randint(1, len(self.droppable_items) ** 2)
        index = index % (len(self.droppable_items) * 3)
        if index < len(self.droppable_items):
            string = type(self.droppable_items[index]).__name__
            string += " item was dropped - want to pick it up?\nY/N\n"
            decision = input(string)
            if decision.upper().strip() == "Y":
                try:
                    self.__player.pick_up(self.droppable_items[index])
                except PickingError as PE:
                    print(str(PE))
                self.droppable_items.remove(self.droppable_items[index])
            else:
                print("Item was not picked up!\n")


    def consumables(self):
        self.post_combat_drops()
        consumable = self.level_specific_consumable[self.__level]
        number_of_consumable = consumable[1]
        type_of_consumable = consumable[0]()
        print(number_of_consumable, type(type_of_consumable).__name__, "\bs found!")
        for i in range(number_of_consumable):
            self.__player.pick_up(type_of_consumable)
        self.out_of_combat()

    def play(self):
        while not self.__dead:
            if self.__in_combat:
                if self.__exit:
                    break
                self.level()

                self.__level += 1
                self.__in_combat = False
            else:
                self.consumables()
                if self.__exit:
                    break
                self.__in_combat = True

    def save(self):
        self.__player.save_level_and_status(self.__level, self.__save_file)

    def load(self):
        self.__level = self.__player.load_save_file(self.__save_file)

    def get_player(self):
        return self.__player

    def set_level(self, value):
        self.__level = value

    def set_cheats(self):
        self.__hasCheated = True