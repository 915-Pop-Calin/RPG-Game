from Abilities.HumanAbilities.Bolster import Bolster
from Abilities.HumanAbilities.Strengthen import Strengthen
from Abilities.HumanAbilities.Taunt import Taunt
from Characters.Character import Character
from Exceptions.exceptions import PickingError, ItemError
from Items.Armors.Armour import Armour
from Items.Armors.Bandage import WornBandage
from Items.Armors.Cloth import Cloth
from Items.Armors.TemArmor import TemArmor
from Items.Potion.HealthPotion import HealthPotion
from Items.Potion.Potion import Potion
from Items.Weapons.Eclipse import Eclipse
from Items.Weapons.LanguageHacker import LanguageHacker
from Items.Weapons.TacosWhisper import TacosWhisper
from Items.Weapons.ToyKnife import ToyKnife
from Items.Weapons.Weapon import Weapon
from Items.Weapons.Words import Words


class HumanPlayer(Character):
    def __init__(self, name):
        super().__init__(name, 3, 0, ToyKnife(), WornBandage(), 20)
        self.__level = 1
        self.__inventory = [None, None, None, None, None, None, None, None]
        self.ids = {100: HealthPotion, 200: ToyKnife, 201: Eclipse, 202: LanguageHacker, 203: TacosWhisper, 204: Words, 300: WornBandage, 301: Cloth, 302: TemArmor}
        self.add_ability("taunt", self.taunt)
        self.add_ability("bolster", self.bolster)
        self.add_ability("strengthen", self.strengthen)

    def find_nonempty_position_in_inventory(self):
        for index in range(len(self.__inventory)):
            if self.__inventory[index] is None:
                return index
        return -1

    def pick_up(self, item):
        index = self.find_nonempty_position_in_inventory()
        if index == -1:
            raise PickingError("Cannot pick up, inventory full")
        self.__inventory[index] = item

    def use_item(self, item_index):
        if item_index < 0 or item_index > len(self.__inventory):
            raise ItemError("Invalid Item!")
        item = self.__inventory[item_index]
        if item is None:
            raise ItemError("Invalid Item!")
        if isinstance(item, Weapon):
            old_weapon = self.change_weapon(item)
            self.__inventory[item_index] = old_weapon
            self.re_set_attack_health()
        if isinstance(item, Armour):
            old_armour = self.change_armour(item)
            self.__inventory[item_index] = old_armour
            self.re_set_attack_health()
        if isinstance(item, Potion):
            self.__inventory[item_index] = None
            item.use(self)

    def taunt(self, opponent, list_of_turns, turn_counter):
        ability = Taunt()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def bolster(self, opponent, list_of_turns, turn_counter):
        ability = Bolster()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def strengthen(self, opponent, list_of_turns, turn_counter):
        ability = Strengthen()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def level_up(self):
        self.__level += 1
        self._health += 5
        self._max_health += 5

    def get_level(self):
        return self.__level

    def print_inventory(self):
        string = ""
        for element in self.__inventory:
            if element == None:
                string += "Empty Place\n"
            else:
                string += str(element)
                string += "\n"
        return string

    def set_up(self, name, attack, defense, weapon, armour, health, level, inventory):
        self._name = name
        self._innate_attack = attack
        self._innate_defense = defense
        self._weapon = weapon
        self._armor = armour
        self._health = health
        self._level = level
        self.__inventory = inventory
        self.re_set_attack_health()

    def save_level_and_status(self, level, filename):
        saved_level = level
        name = self._name
        attack = self._innate_attack
        defense = self._innate_defense
        weapon = self._weapon.get_id()
        armour = self._armor.get_id()
        health = self._health
        inventory = []
        for element in self.__inventory:
            if element is None:
                inventory.append(0)
            else:
                inventory.append(element.get_id())

        with open(filename, 'w') as file:
            line = str(saved_level) + ";" + str(name) + ";" + str(attack) + ";" + str(defense) + ";" + str(weapon) + ";" + str(armour) + ";" + str(health) + ";"
            for index in range (len(inventory)):
                line += str(inventory[index])
                if index != len(inventory) - 1:
                    line += ";"
            file.write(line)

    def load_save_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            line = lines[0]
            line = line.split(";")
            saved_level = int(line[0])
            name = line[1]
            attack = int(line[2])
            defense = int(line[3])
            weapon_id = int(line[4])
            weapon = self.ids[weapon_id]()
            armour_id = int(line[5])
            armour = self.ids[armour_id]()
            health = float(line[6])
            level = int(line[7])
            inventory = []
        for index in range(7, 15):
            if int(line[index]) == 0:
                inventory.append(None)
            else:
                inventory.append(self.ids[int(line[index])]())
        self.set_up(name, attack, defense, weapon, armour, health, level, inventory)
        return saved_level

    def learn_ability(self, ability_name, ability_efect):
        self.add_ability(ability_name, ability_efect)
        string = str(ability_name) + " has been learnt!\n"
        return string