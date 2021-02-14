from CombatSystem.Combat import Combat
from Items.Weapons.OrbOfTheTitans import OrbOfTheTitans


class LastBossCombat(Combat):
    def __init__(self, last_boss):
        super().__init__(last_boss)
        self._options = self._player.get_options()

    def combat(self, human_player):
        boolean, level = self._player.check_if_form_change()
        if boolean:
            if level == 2:
                self.second_phase(human_player)
            elif level == 3:
                self.third_phase(human_player)
                string = self.intervention(human_player)
                print(string)
        else:
            string = self._options[self._player.attack_type()](human_player)
            print(string)

    def second_phase(self, human_player):
        print("ENOUGH of this!\n")
        print("You have NO chances of defeating me!")
        human_player.delete_options()
        print("All your abilities have been deleted!")
        self._player.set_attack_type("physical")

    def third_phase(self, human_player):
        print("You really can't get enough, can you?")
        print("Behold then, my ultimate form!")
        self._player.set_ultimate_form()
        self._player.set_attack_type("both")

    def intervention(self, human_player):
        string = human_player.get_name() + " look, I have no time but I have been studying this for some time.\n"
        string += "And I have came to the conclusion there is only ONE way to beat him.\n"
        string += "You have to use this titan construct to strike him right in the heart.\n"
        human_player.direct_equip(OrbOfTheTitans())
        string += "You have equipped OrbOfTheTitans!\n"
        return string