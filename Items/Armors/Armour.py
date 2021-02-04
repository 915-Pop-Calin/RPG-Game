class Armour:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense

    def attack_value(self):
        return self.__attack

    def defense_value(self):
        return self.__defense

    def __str__(self):
        return str(type(self).__name__) + " ARMOUR: " + str(self.__attack) + " ATTACK, " + str(self.__defense) + " DEFENSE"