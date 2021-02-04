class Item:
    def __init__(self, attack, defense):
        self.__attack = attack
        self.__defense = defense

    def attack_value(self):
        return self.__attack

    def defense_value(self):
        return self.__defense