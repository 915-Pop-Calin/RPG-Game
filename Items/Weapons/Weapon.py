class Weapon:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense
        self.__life_steal = None
        self.__effect = None
        self._dot_effect = None
        self._crit_chance = 0
        self._description = None

    def has_effect(self):
        return self.__effect

    def set_effect(self):
        self.__effect = True

    def attack_value(self):
        return self.__attack

    def defense_value(self):
        return self.__defense

    def __str__(self):
        string = str(type(self).__name__) + " WEAPON: " + str(self.__attack) + " ATTACK, " + str(self.__defense) + " DEFENSE"
        if self._description is not None:
            string += ", " + self._description
        return string

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

    def increment_attack_value(self):
        self.__attack += 1

    def set_attack(self, value):
        self.__attack = value