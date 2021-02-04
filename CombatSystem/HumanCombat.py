from CombatSystem.Combat import Combat


class HumanCombat(Combat):
    def __init__(self, human_player):
        super().__init__(human_player)

    def combat(self, computer_player):
        invalid_input = True
        while invalid_input:
            command = input("your command is:\n")
            if command in self._options:
                string = self._options[command](computer_player, self._list_of_turns, self._turn_counter)
                print(string)
                invalid_input = False
            elif command == "check stats":
                print(computer_player.print_stats())
            elif command == "equip item":
                print(self._player.print_inventory())
                index = int(input("the index of the item you want to equip: \n"))
                self._player.use_item(index)
                invalid_input = False
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