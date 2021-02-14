class Armour:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense
        self.__effect = None
        self.__dodge = 0
        self._description = None

    def attack_value(self):
        return self.__attack

    def has_effect(self):
        return self.__effect

    def set_effect(self):
        self.__effect = True

    def defense_value(self):
        return self.__defense

    def set_defense(self, value):
        self.__defense = value

    def __str__(self):
        string = str(type(self).__name__) + " ARMOUR: " + str(self.__attack) + " ATTACK, " + str(self.__defense) + " DEFENSE "
        if self._description is not None:
            string += "," + self._description
        return string

    def get_dodge(self):
        return self.__dodge

    def set_dodge(self, value):
        self.__dodge = value