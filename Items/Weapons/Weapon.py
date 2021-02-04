class Weapon:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense
        self.__life_steal = None
        self.__effect = None

    def has_effect(self):
        return self.__effect

    def set_effect(self):
        self.__effect = True

    def attack_value(self):
        return self.__attack

    def defense_value(self):
        return self.__defense

    def __str__(self):
        return str(type(self).__name__) + " WEAPON: " + str(self.__attack) + " ATTACK, " + str(self.__defense) + " DEFENSE"

    def get_life_steal(self):
        return self.__life_steal

    def set_life_steal(self, value):
        self.__life_steal = value
