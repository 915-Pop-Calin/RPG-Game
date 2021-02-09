class Weapon:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense
        self.__life_steal = None
        self.__effect = None
        self._dot_effect = None
        self._crit_chance = 0

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

    def set_dot_effect(self, list):
        self._dot_effect = list

    def get_dot_effect(self):
        return self._dot_effect

    def get_crit_chance(self):
        return self._crit_chance