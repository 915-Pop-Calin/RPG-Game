from Characters.Character import Character

class Combat:
    def __init__(self, player):
        self._player = player
        self._options = player.get_options()
        self._list_of_turns = {}
        self._turn_counter = 0

    def check_stun(self):
        if self._player.isStunned():
            print(self._player.get_name(), "\b's turn was skipped because he was stunned!\n")
            self._turn_counter += 1
            return True
        return False

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

    def dot_check(self, second_player):
        dot_effects = self._player.get_dot_effects()
        string = ""
        if len(dot_effects) != 0:
            index = 0
            while index < len(dot_effects):
                self._player.reduce_hp(dot_effects[index][0])
                string += self._player.get_name() + " has taken " + str(dot_effects[index][0]) + " damage over time damage!\n"
                left_turns = dot_effects[index][1]
                self._player.remove_turn_dot(index)
                if left_turns != 1:
                    index += 1

        if self._player.get_hp() < 0:
            return string, None
        return string, True