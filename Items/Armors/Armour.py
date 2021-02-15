class Armour:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense
        self.__effect = None
        self.__dodge = 0
        self._description = None
        self._passive = None
        self._reflector = False

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

    def has_passive(self):
        return self._passive

    def set_passive(self):
        self._passive = True

    def set_dodge(self, value):
        self.__dodge = value

    def set_reflector(self):
        self._reflector = True

    def get_reflector(self):
        return self._reflector