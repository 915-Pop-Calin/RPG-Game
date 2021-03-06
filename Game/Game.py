import random
import termcolor
import texttable

from Characters.Cthulhu import Cthulhu
from Characters.HumanPlayer import HumanPlayer
from Characters.Icarus import Icarus
from Characters.Sauron import Sauron
from Characters.SpaghettiMonster import SpaghettiMonster
from Characters.Tem import Tem
from Characters.YoggSaron import YoggSaron
from Cheats.Cheats import Cheats
from Combat.Combat import Combat
from Exceptions.exceptions import ShoppingError, ItemError, PickingError, LoadingError, DroppingError, SavingError
from FinalLevel.LastLevel import LastLevel
from Items.Potion.GrainOfSalt import GrainOfSalt
from Items.Potion.HealthPotion import HealthPotion
from Items.Potion.SanityPotion import SanityPotion
from SaveFile.SaveFile import SaveFile
from Shop.Shop import Shop


class Game:
    def __init__(self):
        self.__player = None
        self.__dead = False
        self.__enemy = None
        self.__combat = None
        self.__in_combat = True
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
        self.__list_of_save_files = [SaveFile(0), SaveFile(1), SaveFile(2), SaveFile(3), SaveFile(4),
                                     SaveFile(5), SaveFile(6), SaveFile(7), SaveFile(8), SaveFile(9)]


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
            except SavingError as SE:
                print(str(SE))
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

    def print_menu(self):
        table = texttable.Texttable()
        table.set_cols_align(["l", "r", "c"])
        table.add_row(["Game Options", "Player Options", "Shop Options"])
        print(table.draw())

    def print_game_options(self):
        table = texttable.Texttable()
        table.set_cols_align(["l", "r", "c", "c"])
        table.add_row(["proceed", "save", "exit", "back"])
        print(table.draw())

    def print_player_options(self):
        table = texttable.Texttable()
        table.set_cols_align(["l", "r", "c", "c", "c", "c"])
        table.add_row(["equip item", "drop item", "check stats", "drop current item", "see abilities", "back"])
        print(table.draw())

    def print_shop_options(self):
        table = texttable.Texttable()
        table.set_cols_align(["l", "r", "c"])
        table.add_row(["buy", "sell", "back"])
        print(table.draw())

    def out_of_combat(self):
        self.__shop = Shop(self.__player, self.__level)
        decision = None
        while decision != "proceed":
            self.print_menu()
            decision = input()
            decision = decision.lower().strip()
            try:
                if decision == "game options":
                    self.print_game_options()
                    decision = input()
                    if decision == "proceed" or decision == "back":
                        pass
                    elif decision == "save":
                        if self.__hasCheated:
                            print("Game cannot be saved because you cheated!\n")
                        else:
                            self.save()
                    elif decision == "exit":
                        self.__exit = True
                        break
                    else:
                        print("Invalid command!")
                elif decision == "player options":
                    self.print_player_options()
                    decision = input()
                    if decision == "equip item":
                        print(self.__player.print_inventory())
                        item = input("the item you want to equip:\n")
                        if item == "back":
                            pass
                        else:
                            string = self.__player.use_item(item)
                            print(string)
                    elif decision == "drop item":
                        print(self.__player.print_inventory())
                        item = input("the item you want to drop:\n")
                        if item == "back":
                            pass
                        else:
                            string = self.__player.drop_item(item)
                            print(string)
                    elif decision == "check stats":
                        print(self.__player.print_stats())
                    elif decision == "drop current item":
                        choice = input("Drop Weapon or Armour? W/A\n")
                        choice = choice.lower().strip()
                        if choice == "w":
                            self.__player.move_weapon_to_inventory()
                        elif choice == "a":
                            self.__player.move_armour_to_inventory()
                        else:
                            print("Invalid Input!\n")
                    elif decision == "see abilities":
                        self.__player.print_abilities_description()
                    elif decision == "back":
                        pass
                    else:
                        print("Invalid command!\n")
                elif decision == "shop options":
                    self.print_shop_options()
                    decision = input()
                    if decision == "buy":
                        self.__shop.buy_item()
                    elif decision == "sell":
                        self.__shop.sell_item()
                    elif decision == "back":
                        pass
                    else:
                        print("Invalid command!\n")
                elif decision in self.__cheats.list_of_cheats.keys():
                    string = self.__cheats.list_of_cheats[decision](self)
                    print(string)
                    self.__shop = Shop(self.__player, self.__level)
                else:
                    print("Invalid command!\n")
            except SavingError as SE:
                print(str(SE))
            except ItemError as IE:
                print(str(IE))
            except ShoppingError as SE:
                print(str(SE))
            except PickingError as PE:
                print(str(PE))
            except DroppingError as DE:
                print(str(DE))

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
            #if not self.__hasCheated:
            self.__last_level = LastLevel(self.__player, self.__past_selves)
            self.__last_level.play_out()
            #else:
            #    print("Last level cannot be played because you cheated!\n")

    def print_all_save_files(self):
        table = texttable.Texttable()
        table.add_row(["Save Files:"])
        for i in range(len(self.__list_of_save_files)):
            table.add_row([str(self.__list_of_save_files[i])])
        print(table.draw())

    def save(self):
        print("Choose the number of the Save File to save on:\n")
        self.print_all_save_files()
        #for savefile in self.__list_of_save_files:
        #    print(savefile)
        choice = int(input())
        if not (0<=choice<=9):
            raise SavingError("Invalid Save File!")
        list_of_information = [self.__player, self.__level]
        for past_self in self.__past_selves:
            list_of_information.append(past_self)
        self.__list_of_save_files[choice].save_info(list_of_information)

    def load(self):
        '''self.__level, selves = self.__player.load_save_file(self.__save_file)
        self.__past_selves = []
        for past_self in selves:
            if past_self is not None:
                self.__past_selves.append(past_self)
        self.__shop = Shop(self.__player, self.__level)'''
        print("Choose the number of the Save File to load:\n")
        self.print_all_save_files()
        #for savefile in self.__list_of_save_files:
        #    print(savefile)
        choice = int(input())
        if not (0<=choice<=9):
            raise SavingError("Invalid Save File!\n")
        list_of_information = self.__list_of_save_files[choice].load_info()
        length = len(list_of_information)
        if length == 0:
            raise SavingError("Cannot Load Empty File!\n")
        self.__player = list_of_information[0]
        self.__level = list_of_information[1]
        self.__past_selves = []
        for index in range(2, length):
            self.__past_selves.append(list_of_information[index])
        self.__shop = Shop(self.__player, self.__level)

    def get_player(self):
        return self.__player

    def set_level(self, value):
        self.__level = value

    def set_cheats(self):
        self.__hasCheated = True
