import texttable

from CombatSystem.Combat import Combat
from Exceptions.exceptions import CastingError, ItemError


class HumanCombat(Combat):
    def __init__(self, human_player):
        super().__init__(human_player)

    def print_menu(self):
        table = texttable.Texttable()
        table.set_cols_align(["l", "r", "c", "c"])
        table.add_row(["attack", "check stats", "equip item", "actions"])
        print(table.draw())

    def print_actions(self):
        table = texttable.Texttable()
        for option in self._player.get_options().keys():
            if option != "attack":
                table.add_row([option + "\n"])
        print(table.draw())

    def combat(self, computer_player):
        invalid_input = True
        while invalid_input:
            self.print_menu()
            command = input("your command is:\n")
            command = command.lower().strip()
            if command == "actions":
                self.print_actions()
                new_command = input("your action is:\n")
                if new_command in self._options.keys() and new_command != "attack":
                    try:
                        string = self._options[new_command](computer_player, self._list_of_turns, self._turn_counter)
                        print(string)
                        invalid_input = False
                    except CastingError as CE:
                        print(str(CE))
                else:
                    print("Invalid action!\n")
            elif command == "attack":
                string = self._options["attack"](computer_player, self._list_of_turns, self._turn_counter)
                print(string)
                invalid_input = False
            #if command in self._options:
            #    try:
            #        string = self._options[command](computer_player, self._list_of_turns, self._turn_counter)
            #        print(string)
            #        invalid_input = False
            #    except CastingError as CE:
            #        print(str(CE))
            elif command == "check stats":
                print(computer_player.print_stats())
            elif command == "equip item":
                try:
                    print(self._player.print_inventory())
                    item = input("the item you want to equip:\n")
                    string = self._player.use_item(item)
                    print(string)
                    invalid_input = False
                except ItemError as IE:
                    print(str(IE))
            #elif command == "pass":
            #    invalid_input = False
            #elif command == "print level":
            #    self._player.print_lvl()
            else:
                print("Invalid command")
        self._turn_counter += 1

    def post_combat(self):
        self._player.level_up()
        print("LEVEL UP! Level ", self._player.get_level())
        self._list_of_turns = {}
        self._turn_counter = 0

    def update_abilities(self):
        self.options = self._player.get_options()