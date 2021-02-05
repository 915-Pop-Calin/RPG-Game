class Combat:
    def __init__(self, player):
        self._player = player
        self._options = player.get_options()
        self._list_of_turns = {}
        self._turn_counter = 0

    def check_undos(self, second_player):
        if self._turn_counter in list(self._list_of_turns.keys()):
            list_of_actions = self._list_of_turns[self._turn_counter]
            for action in list_of_actions:
                string = action(self._player, second_player)
                print(string)
            del self._list_of_turns[self._turn_counter]

    def fight_end(self, second_player):
        if len(self._list_of_turns.keys()) != 0:
            actions = []
            for key in self._list_of_turns.keys():
                for action in self._list_of_turns[key]:
                    actions.append(action)
            for action in actions:
                string = action(self._player, second_player)
                print(string)

    ''' def check_undos(self, second_player):
        if self._turn_counter in list(self._list_of_turns.keys()):
            string = self._list_of_turns[self._turn_counter](self._player, second_player)
            print(string)
            del self._list_of_turns[self._turn_counter]

    def fight_end(self, second_player):
        if len(self._list_of_turns.keys()) != 0:
            actions = []
            for key in self._list_of_turns.keys():
                actions.append(self._list_of_turns[key])
            for action in actions:
                string = action(self._player, second_player)
                print(string)'''

