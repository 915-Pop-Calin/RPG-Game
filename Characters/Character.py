import random

from Exceptions.exceptions import StunError
from Items.Armors.Armour import Armour
from Items.Armors.LastStand import LastStand
from Items.Armors.LevelFive.EyeOfSauron import EyeOfSauron
from Items.Armors.LevelFour.FireDeflector import FireDeflector
from Items.Armors.LevelFour.Scales import Scales
from Items.Armors.LevelFour.TidalArmour import TidalArmour
from Items.Armors.LevelOne.Bandage import WornBandage
from Items.Armors.LevelOne.Cloth import Cloth
from Items.Armors.LevelOne.TemArmor import TemArmor
from Items.Armors.LevelThree.BootsOfDodge import BootsOfDodge
from Items.Armors.LevelTwo.SteelPlateau import SteelPlateau
from Items.Armors.NinjaYoroi import NinjaYoroi
from Items.Potion.DefensePotion import DefensePotion
from Items.Potion.GrainOfSalt import GrainOfSalt
from Items.Potion.HealthPotion import HealthPotion
from Items.Potion.OffensePotion import OffensePotion
from Items.Potion.SanityPotion import SanityPotion
from Items.Weapons.DoubleEdgedSword import DoubleEdgedSword
from Items.Weapons.Dreams import Dreams
from Items.Weapons.GiantSlayer import GiantSlayer
from Items.Weapons.LevelFive.InfinityEdge import InfinityEdge
from Items.Weapons.LevelFive.RadusBiceps import RadusBiceps
from Items.Weapons.LevelFour.IcarusesTouch import IcarusesTouch
from Items.Weapons.LevelOne.Eclipse import Eclipse
from Items.Weapons.LevelOne.ToyKnife import ToyKnife
from Items.Weapons.LevelOne.Words import Words
from Items.Weapons.LevelSix.TheRing import TheRing
from Items.Weapons.LevelThree.BoilingBlood import BoilingBlood
from Items.Weapons.LevelThree.LanguageHacker import LanguageHacker
from Items.Weapons.LevelThree.TankBuster import TankBuster
from Items.Weapons.LevelThree.Xalatath import Xalatath
from Items.Weapons.LevelTwo.TacosWhisper import TacosWhisper
from Items.Weapons.LevelTwo.TitansFindings import TitansFindings
from Items.Weapons.TwoHandedMace import TwoHandedMace
from Items.Weapons.Weapon import Weapon


class Character:
    def __init__(self, name, innate_attack, innate_defense, weapon, armor, health, description = None):
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
        #self._stunned = False
        self._dot_effects = []
        self._sanity = 100
        self._is_autoattacker = True
        self._stun_resistant = False
        self.ids = {100: HealthPotion, 102: GrainOfSalt, 103: SanityPotion, 104: DefensePotion, 105: OffensePotion,
                    200: ToyKnife, 201: Eclipse, 202: LanguageHacker, 203: TacosWhisper, 204: Words, 205: BoilingBlood,
                    206: IcarusesTouch, 207: TankBuster, 208: InfinityEdge, 209: Dreams, 210: TheRing, 211: TitansFindings,
                    212: Xalatath, 213: RadusBiceps, 214: DoubleEdgedSword, 215: GiantSlayer, 216: TwoHandedMace,
                    300: WornBandage, 301: Cloth, 302: TemArmor, 303: SteelPlateau, 304: BootsOfDodge, 305: Scales,
                    306: EyeOfSauron, 307: TidalArmour, 308: FireDeflector, 309: NinjaYoroi, 310: LastStand}

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
        self._max_health -= value
        self._health = min(self._max_health, self._health)

    def get_multiplier(self, opponent):
        armour = opponent.get_armour()
        if armour >= 0:
            counted_armour = armour * (1 - self._armor_pen)
            multiplier = 100 / (100 + counted_armour)
        else:
            multiplier = 2 - 100 / (100 - armour)
        return multiplier

    def attack(self, opponent):
        multiplier = self.get_multiplier(opponent)
        if self._attack >= 0:
            damage = self._attack
        else:
            damage = 0
        damage *= multiplier
        opponent.reduce_hp(damage)
        return damage

    def critical_attack(self, opponent):
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
        string += str(self._weapon)
        string += str(self._armor)
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
        if self._stun_resistant:
            raise StunError("Cannot stun a Stun Resistant target!\n")
        self._stunned += 1

    def isStunned(self):
        return self._stunned != 0

    def unstun(self):
        self._stunned -= 1

    def add_dot_effect(self, list):
        self._dot_effects.append(list.copy())

    def remove_turn_dot(self, index):
        self._dot_effects[index][1] -= 1
        if self._dot_effects[index][1] == 0:
            self._dot_effects.remove(self._dot_effects[index])

    def get_dot_effects(self):
        return self._dot_effects

    def decrease_dot_effects(self, value):
        for index in range(len(self._dot_effects)):
            self._dot_effects[index][0] = max(1, self._dot_effects[index][0] - value)

    def get_max_hp(self):
        return self._max_health

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

    def get_armour_pen(self):
        return self._armor_pen

    def set_armour_pen(self, value):
        self._armor_pen = value

    def increase_armour_pen(self, value):
        self._armor_pen = min(self._armor_pen + value, 1)

    def set_stun_resistant(self, boolean):
        self._stun_resistant = boolean

    def delete_options(self):
        self._options = {"attack": self.hit}

    def save_character(self, filename):
        name = self._name
        attack = self._innate_attack
        defense = self._innate_defense
        weapon = self._weapon.get_id()
        armour = self._armor.get_id()
        health = self._health
        description = self._description
        with open(filename, "a") as file:
            line = str(name) + ";" + str(attack) + ";" + str(defense) + ";" + str(weapon) + ";" + str(armour) + ";" + str(health) + ";" + str(description)
            line += "\n"
            file.write(line)

    def load_character(self, filename, line_counter):
        with open(filename, 'r') as file:
            lines = file.readlines()
            line = lines[line_counter]
            line = line.split(";")
            name = line[0]
            attack = int(line[1])
            defense = int(line[2])
            weapon_id = int(line[3])
            weapon = self.ids[weapon_id]()
            armor_id = int(line[4])
            armor = self.ids[armor_id]()
            health = float(line[5])
            description = line[6]
            chara = Character(name, attack, defense, weapon, armor, health, description)
            return chara

    def direct_equip(self, item):
        if isinstance(item, Weapon):
            self._weapon = item
        if isinstance(item, Armour):
            self._armor = item