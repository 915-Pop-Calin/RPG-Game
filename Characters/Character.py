import random

from Exceptions.exceptions import StunError
from Items.Armors.Armour import Armour
from Items.Weapons.Weapon import Weapon


class Character:
    def __init__(self, name, innate_attack, innate_defense, weapon, armor, health, description = None):
        """
        We initialise the character with given attributes.
        :param name: a string of characters which represents how the character will be called from now on.
        :param innate_attack: integer representing the innate attack our character has, meaning without any attack enhancers like weapons.
        :param innate_defense: integer representing the innate defense our character has, meaning without any defense enchanters like armours.
        :param weapon: an object of a class that inherits the class Weapon.
        :param armor: an object of a class that inherits the class Armour.
        :param health: integer representing the health our character will start with (so, maximum health as well).
        :param description: who is the character, from a lore viewpoint.
        """
        self._name = name
        self._innate_attack = innate_attack
        self._innate_defense = innate_defense
        self._innate_crit_chance = 0.15
        self._weapon = weapon
        self._armor = armor
        self._innate_armor_pen = 0
        self._armor_pen = self._weapon.get_armor_pen()
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
        self._saved_armor_pen = self._armor_pen
        self._stunned = 0
        self._dot_effects = []
        self._sanity = 100
        self._is_autoattacker = True
        self._stun_resistant = False

    def set_defense_and_armour_to_normal(self):
        self._attack = self._saved_attack
        self._defense = self._saved_armor
        self._armor_pen = self._saved_armor_pen

    def set_attack_value(self, value):
        self._attack = value

    def set_defense_value(self, value):
        self._defense = value

    def get_innate_attack(self):
        return self._innate_attack

    def get_innate_defense(self):
        return self._innate_defense

    def set_innate_attack(self, value):
        self._innate_attack = value
        self.re_set_attack_health()

    def set_innate_defense(self, value):
        self._innate_defense = value
        self.re_set_attack_health()

    def set_innate_health(self, value):
        self._health = value
        self._max_health = value

    def set_hp(self, value):
        self._health = value

    def get_saved_attack(self):
        return self._saved_attack

    def get_saved_armor(self):
        return self._saved_armor

    def get_saved_armor_pen(self):
        return self._armor_pen

    def re_set_attack_health(self):
        self._attack = self._innate_attack + self._weapon.attack_value() + self._armor.attack_value()
        self._defense = self._innate_defense + self._weapon.defense_value() + self._armor.defense_value()
        self._armor_pen = self._armor_pen = self._weapon.get_armor_pen()
        self._saved_armor = self._defense
        self._saved_attack = self._attack
        self._saved_armor_pen = self._armor_pen
        self._crit_chance = self._innate_crit_chance + self._weapon.get_crit_chance()

    def decrease_attack_value(self, value):
        self._attack = self._attack - value

    def decrease_defense_value(self, value):
        self._defense = self._defense - value

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

    def permanently_reduce_hp(self, value):
        """
        The health points of the character are permanently reduced by value.
        :param value: an integer which represents how much the health points will be reduced by
        """
        self._max_health -= value
        self._health = min(self._max_health, self._health)

    def get_multiplier(self, opponent):
        """
        The amount of damage that goes through, with relation to the character's armour penetration and opponent's defense values.
        :param opponent: an object of the class Character
        :return: the multiplier as a percentage
        """
        armour = opponent.get_armour()
        if armour >= 0:
            counted_armour = armour * (1 - self._armor_pen)
            multiplier = 100 / (100 + counted_armour)
        else:
            multiplier = 2 - 100 / (100 - armour)
        return multiplier

    def attack(self, opponent):
        """
        Taking into account the multiplier, this counts how much damage a normal attack would do
        :param opponent: an object of the class Character
        :return: an integer representing the amount of damage a normal attack would do
                """
        multiplier = self.get_multiplier(opponent)
        if self._attack >= 0:
            damage = self._attack
        else:
            damage = 0
        damage *= multiplier
        opponent.reduce_hp(damage)
        return damage

    def critical_attack(self, opponent):
        """
        Taking into account the multiplier, this counts how much damage a critical attack would do
        :param opponent: an object of the class Character
        :return: an integer representing the amount of damage a critical attack would do
        """
        multiplier = self.get_multiplier(opponent)
        if self._attack >= 0:
            damage = self._attack
        else:
            damage = 0
        damage *= multiplier
        damage *= 2
        opponent.reduce_hp(damage)
        return damage

    def deal_damage(self, opponent, damage):
        """
        This deals flat damage to the opponent.
        :param opponent: an object of the class Character
        :param damage: a float number which represents how much damage the opponent will take
        """
        opponent.reduce_hp(damage)

    def life_steal(self, damage):
        """
        If the character's weapon has life steal, he heals proportionally with relation to the damage done.
        :param damage: a float number which represents the damage done
        :return: the string of theactions done
        """
        life_steal_value = self._weapon.get_life_steal()
        life_stolen = life_steal_value * damage
        self.heal(life_stolen)
        string = self._name + " has healed for " + str(round(life_stolen,2)) + "!\n"
        return string

    def hit(self, opponent, list_of_turns, turn_counter):
        """
        The character hits an opponent, taking into account multiple factors such as the crit chance of our current
        character, whether the armour or weapon of the opponent are deflectors (that means they take the damage
        instead of a character taking it), whether the opponent has any dodge chance and we let the random function decide what
        happens in the crit chance and dodge chance scenario. Critical hits deal twice the damage compared to normal hits.
        Afterwards, this checks whether our weapon has any effects, and if it does it applies it taking into account the damage
        done and the opponent. This also checks whether our weapon has life steal, so it heals proportionally with the damage
        done, and whether the armour has any effects as well in order for it to apply it. Moreover, it also checks
        if the weapon or armour have any passives, applying them with relation to the caster, opponent, list of turns
        and the turn counter if that's the case. At the end, we return the full string of the actions done for us to
        print it in the end.
        :param opponent: an object of the class Character
        :param list_of_turns: a dictionary whose keys are integer numbers and whose values are abilities that need to be decast later on
        :param turn_counter: an integer which counts the turns
        :return: the string which will be printed later on
        """
        critical = random.randint(1, 100)
        opponent_armor = opponent.get_armor()
        opponent_weapon = opponent.get_weapon()
        dodge_chance = opponent_armor.get_dodge()
        odds = dodge_chance * 100
        random_choice = random.randint(1, 100)
        damage = 0
        if dodge_chance != 0 and random_choice <= odds:
            string = opponent.get_name() + " dodged your attack!\n"
        else:
            if opponent_weapon.get_reflector() and not opponent_weapon.is_broken():
                string = opponent_weapon.take_hit(self._attack)
            elif opponent_armor.get_reflector() and not opponent_armor.is_broken():
                string = opponent_armor.take_hit(self._attack)
            elif critical <= self._crit_chance * 100:
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
            if self._weapon.has_passive() is not None:
                new_string = self._weapon.passive(self, opponent, list_of_turns, turn_counter)
                string += new_string
            if self._armor.has_passive() is not None:
                new_string = self._armor.passive(self, opponent, list_of_turns, turn_counter)
                string += new_string
        return string

    def get_name(self):
        return self._name

    def change_weapon(self, new_weapon):
        """
        The current weapon worn by the character is replaced by a new weapon given as a parameter.
        :param new_weapon: an object of a class which inherits the class Weapon.
        :return: the old weapon
        """
        old_weapon = self._weapon
        self._weapon = new_weapon
        return old_weapon

    def change_armour(self, new_armour):
        """
        The current armour worn by the character is replaced by a new armour given as a parameter.
        :param new_armour: an object of a class which inherits the class Armour
        :return: the old armour
        """
        old_armour = self._armor
        self._armor = new_armour
        return old_armour

    def heal(self, amount_healed):
        """
        The character is healed by amount_healed, but it cannot go over maximum health.
        :param amount_healed: a strictly positive integer which represents how much the character will heal
        """
        self._health = min(self._health + amount_healed, self._max_health)

    def print_stats(self):
        """
        We return the stats as a string to be printed later.
        :return: a string representing the stats of the character
        """
        string = str(self._name) + ": " + str(self._health) + " HEALTH, " + str(self._defense) + " DEFENSE, " + str(self._attack) + " ATTACK"
        if self._description is not None:
            string += '\n'
            string += self._description
        string += str(self._weapon)
        string += str(self._armor)
        return string

    def get_weapon(self):
        return self._weapon

    def get_armor(self):
        return self._armor

    def add_ability(self, ability_name, effect):
        """
        We add an ability to the list of options
        :param ability_name: a string of characters representing the name of the ability
        :param effect: the method of the character class which applies the ability
        """
        self._options[ability_name] = effect

    def get_options(self):
        return self._options

    def get_attack_value(self):
        return self._attack

    def get_defense_value(self):
        return self._defense

    def stun(self):
        """
        We try to stun the target by adding one to the stun stack. If the target is stun resistant, then we raise a StunError so
        it is not stunned.
        """
        if self._stun_resistant:
            raise StunError("Cannot stun a Stun Resistant target!\n")
        self._stunned += 1

    def isStunned(self):
        return self._stunned != 0

    def unstun(self):
        """
        We remove 1 from the stun stack (stun stacks itself, so 0 means not stunned and everything else means stunned).
        """
        self._stunned -= 1

    def add_dot_effect(self, list):
        """
        We add a dot effect to the list of our current dot effects.
        :param list: a list consisting of 2 positive integer numbers, representing the damage taken and the number ofurns we will take the
        damage for, respectively.
        """
        self._dot_effects.append(list.copy())

    def remove_turn_dot(self, index):
        """
        After taking damage, we decrease the amount of turns we will take damage with the DOT and if we have 0 turns left, we remove
        the dot effect.
        :param index: the index which we check
        """
        self._dot_effects[index][1] -= 1
        if self._dot_effects[index][1] == 0:
            self._dot_effects.remove(self._dot_effects[index])

    def get_dot_effects(self):
        return self._dot_effects

    def decrease_dot_effects(self, value):
        """
        For every dot effect which is applied on our character, the damage is reduced by value.
        :param value: an integer number which represents how much each dot effect will be reduced.
        """
        for index in range(len(self._dot_effects)):
            self._dot_effects[index][0] = max(1, self._dot_effects[index][0] - value)

    def get_max_hp(self):
        return self._max_health

    def reduce_sanity(self, value):
        """
        Some sanity is reduced from the character.
        :param value: an integer number representing the sanity that will be reduced.
        """
        self._sanity -= value

    def get_sanity(self):
        return self._sanity

    def restore_sanity(self, value):
        """
        Some sanity is restored to the character, but the sanity of the player cannot go above 100.
        :param value: an integer number representing the sanity that will be restored.
        """
        self._sanity = min(self._sanity + value, 100)

    def is_autoattacker(self):
        return self._is_autoattacker

    def clear_dot_effects(self):
        """
        All dot effects applied on the characters are cleared.
        Required for CleanseDOT ability of HumanPlayer
        """
        self._dot_effects = []

    def get_armour_pen(self):
        return self._armor_pen

    def set_armour_pen(self, value):
        """
        The armour penetration value is set exactly to a value, but it cannot be bigger than 1 or smaller than 0.
        Required for TrueDamage ability of HumanPlayer.
        :param value: a rational number between 0 and 1.
        """
        self._armor_pen = value

    def increase_armour_pen(self, value):
        """
        The armour penetration value is flatly increased by a value, but it cannot be bigger than 1.
        :param value: a rational number between 0 and 1
        """
        self._armor_pen = min(self._armor_pen + value, 1)

    def set_stun_resistant(self, boolean):
        """
        We choose if the character is stun resistant or not.
        Required for the CCImmunity ability of HumanPlayer.
        :param boolean: a boolean value (True or False)
        """
        self._stun_resistant = boolean

    def delete_options(self):
        """
        All of the character's options are deleted, being left only with an attack option.
        This is needed for the last fight, precisely for the phase 2, where the boss removes all of our options.
        """
        self._options = {"attack": self.hit}

    def direct_equip(self, item):
        """
        The character equips an item directly, without having it to pass through the inventory.
        This is needed for the last fight, where the stranger gives the character a weapon he instantly equips.
        :param item: an object of a class which inherits either class Weapon or Armour
        """
        if isinstance(item, Weapon):
            self._weapon = item
        if isinstance(item, Armour):
            self._armor = item
