import random


from CombatSystem.ComputerCombat import ComputerCombat
from CombatSystem.HumanCombat import HumanCombat


class Combat:
    def __init__(self, humanPlayer, computerPlayer):
        self.__humanPlayer = humanPlayer
        self.__computerPlayer = computerPlayer
        self.__turn = 0
        self.__combatDone = False
        self.__list_of_turns = {}
        self.__turn_counter = 0
        self.__dead = False
        self.__human_combat = HumanCombat(self.__humanPlayer)
        self.__computer_combat = ComputerCombat(self.__computerPlayer)

    def print_options(self):
        print("attack\nstrengthen\nbolster\ntaunt\ncheck stats")

    def player_turn(self):
        self.__human_combat.check_undos(self.__computerPlayer)
        self.print_options()
        self.__human_combat.combat(self.__computerPlayer)
        if self.__computerPlayer.get_hp() <= 0:
            print(self.__humanPlayer.get_name(), " has won!")
            self.__human_combat.fight_end(self.__computerPlayer)
            self.__computer_combat.fight_end(self.__humanPlayer)
            self.__human_combat.post_combat()
            self.__combatDone = True
        self.__turn = 1

        self.__turn_counter += 1

    def computer_turn(self):
        self.__computer_combat.check_undos(self.__humanPlayer)
        self.__computer_combat.combat(self.__humanPlayer)
        if self.__humanPlayer.get_hp() <= 0:
            self.__computer_combat.fight_end(self.__humanPlayer)
            self.__human_combat.fight_end(self.__computerPlayer)
            self.__dead = True
            self.__combatDone = True
        self.__turn = 0

    def fight(self):
        while not self.__combatDone:
            if self.__turn == 0:
                self.player_turn()
            else:
                self.computer_turn()

    def isDead(self):
        return self.__dead