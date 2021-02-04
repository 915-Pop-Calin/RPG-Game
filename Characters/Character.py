import random


class Character:
    def __init__(self, name, innate_attack, innate_defense, weapon, armor, health, description = None):
        self._name = name
        self._innate_attack = innate_attack
        self._innate_defense = innate_defense
        self._weapon = weapon
        self._armor = armor
        self._attack = self._innate_attack + self._weapon.attack_value() + self._armor.attack_value()
        self._defense = self._innate_defense + self._weapon.defense_value() + self._armor.defense_value()
        self._health = health
        self._max_health = self._health
        self._description = description
        self._options = {"attack": self.hit}
        self._list_of_turns = {}
        self._turn_counter = 0

    def re_set_attack_health(self):
        self._attack = self._innate_attack + self._weapon.attack_value() + self._armor.attack_value()
        self._defense = self._innate_defense + self._weapon.defense_value() + self._armor.defense_value()

    def decrease_attack_value(self, value):
        self._attack = max(0, self._attack - value)

    def decrease_defense_value(self, value):
        self._defense = max(0, self._defense - value)

    def increase_attack_value(self, value):
        self._attack = self._attack + value

    def increase_defense_value(self, value):
        self._defense = self._defense + value

    def get_hp(self):
        return self._health

    def get_armour(self):
        return self._defense

    def reduce_hp(self, damage_taken):
        self._health -= damage_taken

    def attack(self, opponent):
        multiplier = 100 / (100 + opponent.get_armour())
        damage = self._attack
        damage *= multiplier
        opponent.reduce_hp(damage)
        return damage

    def critical_attack(self, opponent):
        multiplier = 100 / (100 + opponent.get_armour())
        damage = self._attack
        damage *= multiplier
        damage *= 2
        opponent.reduce_hp(damage)
        return damage

    def hit(self, opponent, list_of_turns, turn_counter):
        critical = random.randint(1, 5)
        if critical == 1:
            damage = self.critical_attack(opponent)
            health = round(opponent.get_hp(), 2)
            damage = str(round(damage, 2))
            health_2 = str(health)
            opponent_name = str(opponent.get_name())
            string = "CRITICAL HIT! " + damage + " damage done to " + opponent_name + "!\n"
            string += opponent_name + " is left with " + health_2 + " health!"
        else:
            damage = self.attack(opponent)
            string = str(round(damage, 2)) + " damage done to " + opponent.get_name() + "!\n"
            string += opponent.get_name() + " is left with " + str(round(opponent.get_hp(), 2)) + " health!"
        return string

    def get_name(self):
        return self._name

    def change_weapon(self, new_weapon):
        old_weapon = self._weapon
        self._weapon = new_weapon
        return old_weapon

    def change_armour(self, new_armour):
        old_armour = self._armor
        self._armor = new_armour
        return old_armour

    def heal(self, amount_healed):
        self._health = min(self._health + amount_healed, self._max_health)

    def print_stats(self):
        string = str(self._name) + ": " + str(self._health) + " HEALTH, " + str(self._defense) + " DEFENSE, " + str(self._attack) + " ATTACK"
        if self._description is not None:
            string += '\n'
            string += self._description
        return string

    def get_weapon(self):
        return self._weapon

    def get_armor(self):
        return self._armor

    def add_ability(self, ability_name, effect):
        self._options[ability_name] = effect

    def get_options(self):
        return self._options