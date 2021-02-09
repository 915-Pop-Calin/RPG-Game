import random


class Character:
    def __init__(self, name, innate_attack, innate_defense, weapon, armor, health, description = None):
        self._name = name
        self._innate_attack = innate_attack
        self._innate_defense = innate_defense
        self._innate_crit_chance = 0.15
        self._weapon = weapon
        self._armor = armor
        self._attack = self._innate_attack + self._weapon.attack_value() + self._armor.attack_value()
        self._defense = self._innate_defense + self._weapon.defense_value() + self._armor.defense_value()
        self._crit_chance = self._innate_crit_chance + self._weapon.get_crit_chance()
        self._health = health
        self._max_health = self._health
        self._description = description
        self._options = {"attack": self.hit}
        self._list_of_turns = {}
        self._turn_counter = 0
        self._saved_attack = self._attack
        self._saved_armor = self._defense
        self._stunned = False
        self._dot_effects = []
        self._sanity = 100
        self._is_autoattacker = True

    def set_defense_and_armour_to_normal(self):
        self._attack = self._saved_attack
        self._defense = self._saved_armor

    def set_attack_value(self, value):
        self._attack = value

    def set_defense_value(self, value):
        self._defense = value

    def set_hp(self, value):
        self._health = value

    def get_saved_attack(self):
        return self._saved_attack

    def get_saved_armor(self):
        return self._saved_armor

    def re_set_attack_health(self):
        self._attack = self._innate_attack + self._weapon.attack_value() + self._armor.attack_value()
        self._defense = self._innate_defense + self._weapon.defense_value() + self._armor.defense_value()
        self._saved_armor = self._defense
        self._saved_attack = self._attack
        self._crit_chance = self._innate_crit_chance + self._weapon.get_crit_chance()

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

    def deal_damage(self, opponent, damage):
        opponent.reduce_hp(damage)

    def life_steal(self, damage):
        life_steal_value = self._weapon.get_life_steal()
        life_stolen = life_steal_value * damage
        self.heal(life_stolen)
        string = self._name + " has healed for " + str(round(life_stolen,2)) + "!\n"
        return string

    def hit(self, opponent, list_of_turns, turn_counter):
        critical = random.randint(1, 100)
        opponent_armor = opponent.get_armor()
        dodge_chance = opponent_armor.get_dodge()
        odds = dodge_chance * 100
        random_choice = random.randint(1, 100)
        if dodge_chance != 0 and random_choice <= odds:
                string = opponent.get_name() + " dodged your attack!\n"
        else:
            if critical <= self._crit_chance * 100:
                damage = self.critical_attack(opponent)
                health = round(opponent.get_hp(), 2)
                health_2 = str(health)
                opponent_name = str(opponent.get_name())
                string = "CRITICAL HIT! " + str(round(damage,2)) + " damage done to " + opponent_name + "!\n"
                string += opponent_name + " is left with " + health_2 + " health!\n"

            else:
                damage = self.attack(opponent)
                string = str(round(damage, 2)) + " damage done to " + opponent.get_name() + "!\n"
                string += opponent.get_name() + " is left with " + str(round(opponent.get_hp(), 2)) + " health!\n"
            if self._weapon.has_effect() is not None:
                new_string = self._weapon.effect(damage, self, opponent)
                string += new_string
            if self._weapon.get_life_steal() is not None:
                lifesteal_string = self.life_steal(damage)
                string += lifesteal_string
            if self._armor.has_effect() is not None:
                new_string = self._armor.effect(damage, self, opponent)
                string += new_string
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

    def get_attack_value(self):
        return self._attack

    def get_defense_value(self):
        return self._defense

    def stun(self):
        self._stunned = True

    def isStunned(self):
        return self._stunned

    def unstun(self):
        self._stunned = False

    def add_dot_effect(self, list):
        self._dot_effects.append(list.copy())

    def remove_turn_dot(self, index):
        self._dot_effects[index][1] -= 1
        if self._dot_effects[index][1] == 0:
            self._dot_effects.remove(self._dot_effects[index])

    def get_dot_effects(self):
        return self._dot_effects

    def reduce_sanity(self, value):
        self._sanity -= value

    def get_sanity(self):
        return self._sanity

    def restore_sanity(self, value):
        self._sanity = min(self._sanity + value, 100)

    def is_autoattacker(self):
        return self._is_autoattacker

    def clear_dot_effects(self):
        self._dot_effects = []