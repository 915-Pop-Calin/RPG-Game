import termcolor

from Combat.Combat import Combat
from FinalLevel.FinalBoss import FinalBoss
from FinalLevel.GenocideCombat import GenocideCombat
from SaveFile.SaveFile import SaveFile


class LastLevel:
    def __init__(self, human_player, list_of_past_selves):
        self.__human_player = human_player
        self.__past_selves = list_of_past_selves
        self.__dialogue = ["So this is it.\n", "You have reached the end of your journey.\n", "You have achieved your goal.\n",
                           "You have neutralised the evil in this world.\n", "However, while doing so.\n",
                           "You have succumbed to the darkness you swore to oppose.\n", "And you have became exactly the thing you swore to destroy.\n",
                           "Now, you have your final choice.\n", "You can choose to destroy whatever is left of your humanity.\n",
                           "Or you can spare it.\n", "The decision is yours.\n"]
        self.__final_boss = None
        self.__combat = None


    def play_out(self):
        self.startup()
        decision = self.the_decision()
        if decision == "destroy":
            choice1 = self.young_chara_fight()
            print(choice1)
            if choice1 is not None:
                choice2 = self.teen_chara_fight()
                if choice2 is not  None:
                    choice3 = self.adult_chara_fight()
                    if choice3 is not None:
                        self.delete_save_files()
            print(termcolor.colored("BAD ENDING", "red"))

        if decision == "spare":
            self.spare()
            if not self.__human_player.get_hp() <=0 and not self.__human_player.get_sanity() <= 0:
                print(termcolor.colored("GOOD ENDING", "blue"))
                self.delete_save_files()
            else:
                print(termcolor.colored("BAD ENDING", "red"))

    def delete_save_files(self):
        for index in range (10):
            savefile = SaveFile(index)
            savefile.delete_save_file()

    def startup(self):
        while len(self.__dialogue) != 1:
            print(self.__dialogue[0])
            print("next\n")
            invalid_input = True
            while invalid_input:
                command = input("command:\n")
                if command.lower().strip() == "next":
                    invalid_input = False
                    self.__dialogue.pop(0)

    def the_decision(self):
        print(self.__dialogue[0])
        self.__dialogue.pop(0)
        print("spare\ndestroy\n")
        invalid_input = True
        while invalid_input:
            command = input("command:\n")
            if command.lower().strip() == "destroy":
                return "destroy"
            if command.lower().strip() == "spare":
                return "spare"

    def young_chara_fight(self):
        young_chara = self.__past_selves[0]
        genocide_combat = GenocideCombat(self.__human_player, young_chara)
        return genocide_combat.combat()

    def teen_chara_fight(self):
        teen_chara = self.__past_selves[1]
        genocide_combat = GenocideCombat(self.__human_player, teen_chara)
        return genocide_combat.combat()

    def adult_chara_fight(self):
        adult_chara = self.__past_selves[2]
        genocide_combat = GenocideCombat(self.__human_player, adult_chara)
        return genocide_combat.combat()

    def murdery_decision(self):
        print("Very Well.")

    def spare(self):
        print("A strange figure appears in the shadows.\n")
        print("This is the end.\n")
        self.__final_boss = FinalBoss()
        self.__combat = Combat(self.__human_player, self.__final_boss)
        self.__combat.fight()
