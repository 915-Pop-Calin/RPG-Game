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
        string = "check stats\nequip item\n"
        for option in self.__humanPlayer.get_options().keys():
            string += option
            string += "\n"
        print(string)

    def player_turn(self):
        string, verdict = self.__human_combat.dot_check(self.__computerPlayer)
        print(string)
        if verdict == None:
            self.__dead = True
            self.__combatDone = True
            print(self.__computerPlayer.get_name(), " has won!\n")
        self.__human_combat.check_undos(self.__computerPlayer)
        if not self.__dead and not self.__combatDone:
            self.print_options()
            self.__human_combat.combat(self.__computerPlayer)
            if self.__computerPlayer.get_hp() <= 0:
                minimum_gold_to_gain = (self.__turn_counter + 1) * self.__humanPlayer.get_level() * 20
                maximum_gold_to_gain = (self.__turn_counter + 1) * self.__humanPlayer.get_level() * 40
                gold_to_gain = random.randint(minimum_gold_to_gain, maximum_gold_to_gain)
                self.__humanPlayer.gain_gold(gold_to_gain)
                print(self.__humanPlayer.get_name(), " has won!\n")
                print(self.__humanPlayer.get_name(), " has gained ", str(gold_to_gain), " gold!\n")
                self.__human_combat.fight_end(self.__computerPlayer)
                self.__computer_combat.fight_end(self.__humanPlayer)
                self.__human_combat.post_combat()
                self.__combatDone = True
        self.__turn = 1
        self.__turn_counter += 1

    def computer_turn(self):
        string, verdict = self.__computer_combat.dot_check(self.__humanPlayer)
        print(string)
        if verdict == None:
            self.__combatDone = True
            print(self.__humanPlayer.get_name(), " has won!\n")
        self.__computer_combat.check_undos(self.__humanPlayer)
        if not self.__combatDone:
            self.__computer_combat.combat(self.__humanPlayer)
            if self.__humanPlayer.get_hp() <= 0 or self.__humanPlayer.get_sanity() <= 0:
                print(self.__computerPlayer.get_name(), " has won!\n")
                self.__computer_combat.fight_end(self.__humanPlayer)
                self.__human_combat.fight_end(self.__computerPlayer)
                self.__dead = True
                self.__combatDone = True
        self.__turn = 0

    def fight(self):
        while not self.__combatDone:
            if self.__turn == 0:
                if not self.__humanPlayer.isStunned():
                    self.player_turn()
                else:
                    print(self.__humanPlayer.get_name(), "\b's turn was skipped because he was stunned!\n")
                    self.__turn = 1
            else:
                if not self.__computerPlayer.isStunned():
                    self.computer_turn()
                else:
                    print(self.__computerPlayer.get_name(), "\b's turn was skipped because he was stunned!\n")
                    self.__turn = 0


    def isDead(self):
        return self.__dead