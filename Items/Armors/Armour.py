class Armour:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense
        self.__effect = None
        self.__dodge = 0

    def attack_value(self):
        return self.__attack

    def has_effect(self):
        return self.__effect

    def set_effect(self):
        self.__effect = True

    def defense_value(self):
        return self.__defense

    def __str__(self):
        return str(type(self).__name__) + " ARMOUR: " + str(self.__attack) + " ATTACK, " + str(self.__defense) + " DEFENSE"

    def get_dodge(self):
        return self.__dodge

    def set_dodge(self, value):
        self.__dodge = value