import random

from CombatSystem.Combat import Combat


class ComputerCombat(Combat):
    def __init__(self, computer_player):
        super().__init__(computer_player)

    def combat(self, human_player):
        willAttack = random.randint(1, 4)
        if willAttack == 4:
            choice = random.choice(list(self._options.keys()))
        else:
            choice = "attack"
        string = self._options[choice](human_player, self._list_of_turns, self._turn_counter)
        print(string)
        self._turn_counter += 1


