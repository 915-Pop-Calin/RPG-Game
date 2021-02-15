import math

import termcolor

class GenocideCombat:
    def __init__(self, player_one, player_two):
        self.__human_player = player_one
        self.__computer_player = player_two

    def combat(self):
        print(self.__computer_player.get_name(), "arrives into the fray!\n")
        print(termcolor.colored("MURDER\nspare\nstats\n", "red"))
        invalid_input = True
        while invalid_input:
            decision = input(termcolor.colored("command:\n", "red"))
            if decision == "stats":
                print(self.__computer_player.print_stats())
            elif decision.upper().strip() == "MURDER":
                self.__human_player.deal_damage(self.__computer_player, math.inf)
                string = self.__computer_player.get_name() + " was defeated!\n"
                invalid_input = False
                print(string)
            elif decision.lower().strip() == "spare":
                print("And I thought of you highly.")
                self.__human_player.deal_damage(self.__human_player, math.inf)
                string = self.__human_player.get_name() + " was murdered!\n"
                print(string)
                return None
        return True
