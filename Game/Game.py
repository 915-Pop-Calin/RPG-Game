import random
import termcolor

from Characters.Cthulhu import Cthulhu
from Characters.HumanPlayer import HumanPlayer
from Characters.Icarus import Icarus
from Characters.Sauron import Sauron
from Characters.SpaghettiMonster import SpaghettiMonster
from Characters.Tem import Tem
from Characters.YoggSaron import YoggSaron
from Cheats.Cheats import Cheats
from Combat.Combat import Combat
from Exceptions.exceptions import ShoppingError, ItemError, PickingError, LoadingError
from FinalLevel.LastLevel import LastLevel
from Items.Potion.GrainOfSalt import GrainOfSalt
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
        self.level_specific_enemy ={1: Tem, 2: SpaghettiMonster, 3: YoggSaron, 4: Cthulhu, 5: Icarus, 6: Sauron}
        self.level_specific_consumable = {2: [HealthPotion, 3], 3: [GrainOfSalt, 2], 4: [SanityPotion, 2], 5: [SanityPotion, 2], 6: [GrainOfSalt, 3], 7: [SanityPotion, 2]}
        self.__hasCheated = False
        self.__cheats = Cheats()
        self.__past_selves = []
        self.__level_break_points = {2: ["young ", "does not want to hurt you"], 5: ["teen ", "might want to hurt you"],
                                                                                     7: ["adult ", "wants to MURDER you"]}

    def initialise_game(self):
        decision = input("Do you want to load your save file? Y/N\n")
        if decision.upper().strip() == "Y":
            try:
                self.__player = HumanPlayer("filler")
                self.load()
            except LoadingError as LE:
                print(str(LE))
                name = input("The name you want to use from now on is:\n")
                human = HumanPlayer(name)
                self.__player = human
        else:
            name = input("The name you want to use from now on is:\n")
            human = HumanPlayer(name)
            self.__player = human
        if self.__level == 7:
            self.__last_level = LastLevel(self.__player, self.__past_selves)
            self.__last_level.play_out()
        else:
            self.out_of_combat()

    def out_of_combat(self):
        self.__shop = Shop(self.__player, self.__level)
        decision = None
        while decision != "next":
            decision = input("next\nstats\nequip item\ndrop item\nsave\nsee abilities\nbuy\nsell\nexit\n")
            decision = decision.lower().strip()
            if decision == "stats":
                print(self.__player.print_stats())
            elif decision == "equip item":
                try:
                    print(self.__player.print_inventory())
                    item = input("the item you want to equip:\n")
                    if item == "back":
                        pass
                    else:
                        string = self.__player.use_item(item)
                        print(string)
                except ItemError as IE:
                    print(str(IE))
            elif decision == "drop item":
                try:
                    print(self.__player.print_inventory())
                    item = input("the item you want to drop:\n")
                    if item == "back":
                        pass
                    else:
                        string = self.__player.drop_item(item)
                        print(string)
                except ItemError as IE:
                    print(str(IE))
            elif decision == "save":
                if self.__hasCheated:
                    print("Game cannot be saved because you cheated!\n")
                else:
                    self.save()
            elif decision == "exit":
                self.__exit = True
                break
            elif decision == "see abilities":
                self.__player.print_abilities_description()
            elif decision == "buy":
                try:
                    self.__shop.buy_item()
                except ShoppingError as PE:
                    print(str(PE))
                except PickingError as PE:
                    print(str(PE))
            elif decision == "sell":
                try:
                    self.__shop.sell_item()
                except ShoppingError as SE:
                    print(str(SE))
            elif decision in self.__cheats.list_of_cheats.keys():
                string = self.__cheats.list_of_cheats[decision](self)
                print(string)
                self.__shop = Shop(self.__player, self.__level)
            elif decision != "next":
                print("Invalid Command!")

    def level(self):
        if self.__level >= 7:
            pass
        else:
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
        if self.__level != 8:
            self.post_combat_drops()
            consumable = self.level_specific_consumable[self.__level]
            number_of_consumable = consumable[1]
            type_of_consumable = consumable[0]()
            print(number_of_consumable, type(type_of_consumable).__name__, "\bs found!")
            try:
                for i in range(number_of_consumable):
                    self.__player.pick_up(type_of_consumable)
            except PickingError as PE:
                print(str(PE))
            self.out_of_combat()

    def play(self):
        while not self.__dead and self.__level <= 7:
            if self.__in_combat:
                if self.__exit:
                    break
                self.level()

                self.__level += 1
                self.__in_combat = False
            else:
                if self.__level in self.__level_break_points.keys():
                    status = self.__level_break_points[self.__level][0]
                    description = self.__level_break_points[self.__level][1]
                    current_name = self.__player.get_name()
                    chara = self.__player.create_character_copy(status + current_name, description)
                    self.__past_selves.append(chara)
                self.consumables()
                if self.__level == 7:
                    break
                if self.__exit:
                    break
                self.__in_combat = True
        if self.__level == 7 and not self.__dead and not self.__exit:
            if not self.__hasCheated:
                self.__last_level = LastLevel(self.__player, self.__past_selves)
                self.__last_level.play_out()
            else:
                print("Last level cannot be played because you cheated!\n")

    def save(self):
        self.__player.save_level_and_status(self.__level, self.__save_file)
        for past_self in self.__past_selves:
            past_self.save_character(self.__save_file)

    def load(self):
        self.__level, selves = self.__player.load_save_file(self.__save_file)
        self.__past_selves = []
        for past_self in selves:
            if past_self is not None:
                self.__past_selves.append(past_self)
        self.__shop = Shop(self.__player, self.__level)

    def get_player(self):
        return self.__player

    def set_level(self, value):
        self.__level = value

    def set_cheats(self):
        self.__hasCheated = True