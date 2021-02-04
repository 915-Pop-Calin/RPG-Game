import random

from Characters.HumanPlayer import HumanPlayer
from Characters.SpaghettiMonster import SpaghettiMonster
from Characters.Tem import Tem
from Combat.Combat import Combat
from Items.Potion.ExperiencePotion import ExperiencePotion
from Items.Potion.HealthPotion import HealthPotion


class Game:
    def __init__(self):
        self.__player = None
        self.__dead = False
        self.__consumables = {1: self.level_one_consumables, 2: self.level_two_consumables}
        self.__levels = {1: self.level_one, 2: self.level_two}
        self.__enemy = None
        self.__combat = None
        self.__in_combat = True
        self.__save_file = "saved.txt"
        self.__exit = False
        self.__level = 1
        self.droppable_items = []

    def initialise_game(self):
        decision = input("Do you want to load your save file? Y/N\n")
        if decision == "Y":
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
            decision = input("next\nstats\nequip item\nsave\nexit\n")
            if decision == "stats":
                print(self.__player.print_stats())
            elif decision == "equip item":
                print(self.__player.print_inventory())
                index = int(input("the index of the item you want to equip:\n"))
                self.__player.use_item(index)
            elif decision == "save":
                self.save()
            elif decision == "exit":
                self.__exit = True
                break
            elif decision != "next":
                print("Invalid Command!")

    def level_one(self):
        print("WILD TEM APPEARED!")
        self.__enemy = Tem()
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

    def level_two(self):
        print("WILD SPAGHETTI MONSTER APPEARED!")
        self.__enemy = SpaghettiMonster()
        self.combat()

    def post_combat_drops(self):
        self.drops()
        index = random.randint(1, len(self.droppable_items) ** 2)
        index = index % (len(self.droppable_items) * 3)
        if index < len(self.droppable_items):
            string = type(self.droppable_items[index]).__name__
            string += " item was dropped - want to pick it up?\nY/N\n"
            decision = input(string)
            if decision == "Y":
                self.__player.pick_up(self.droppable_items[index])

    def level_one_consumables(self):
        self.post_combat_drops()
        print("Three health potions found!")
        for i in range(3):
            self.__player.pick_up(HealthPotion())
        self.out_of_combat()

    def level_two_consumables(self):
        self.post_combat_drops()
        print("An experience potion found!")
        self.__player.pick_up(ExperiencePotion())
        self.out_of_combat()

    def play(self):
        while not self.__dead:
            if self.__in_combat:
                if self.__exit:
                    break
                self.__levels[self.__level]()

                self.__level += 1
                self.__in_combat = False
            else:
                self.__consumables[self.__level - 1]()
                if self.__exit:
                    break
                self.__in_combat = True

    def save(self):
        self.__player.save_level_and_status(self.__level, self.__save_file)

    def load(self):
        self.__level = self.__player.load_save_file(self.__save_file)

