import texttable

from Abilities.HumanAbilities.BlindingRage import BlindingRage
from Abilities.HumanAbilities.Bolster import Bolster
from Abilities.HumanAbilities.CCImunity import CCImunity
from Abilities.HumanAbilities.CleanseDOT import CleanseDOT
from Abilities.HumanAbilities.Discourage import Discourage
from Abilities.HumanAbilities.Focus import Focus
from Abilities.HumanAbilities.Strengthen import Strengthen
from Abilities.HumanAbilities.Taunt import Taunt
from Abilities.HumanAbilities.TrueDamage import TrueDamage
from Abilities.TemAbilities.DoNothing import DoNothing
from Characters.Character import Character
from Exceptions.exceptions import PickingError, ItemError, ShoppingError, LoadingError, DroppingError
from Items.Armors.Armour import Armour
from Items.Armors.LevelOne.Bandage import WornBandage
from Items.Armors.NoArmour import NoArmour
from Items.Potion.Potion import Potion
from Items.Weapons.LevelOne.ToyKnife import ToyKnife
from Items.Weapons.NoWeapon import NoWeapon
from Items.Weapons.TwoHandedMace import TwoHandedMace
from Items.Weapons.Weapon import Weapon


class HumanPlayer(Character):
    def __init__(self, name):
        #super().__init__(name, 0, 0, TwoHandedMace(), WornBandage(), 20000)
        super().__init__(name, 10, 0, ToyKnife(), WornBandage(), 20)
        self.__level = 1
        self.__inventory = [None, None, None, None, None, None, None, None]
        self.add_ability("taunt", self.taunt)
        self.add_ability("bolster", self.bolster)
        self.add_ability("strengthen", self.strengthen)
        self.abilities_to_learn = {2: BlindingRage(), 3: Discourage(), 4: Focus(), 5: CleanseDOT(), 6: TrueDamage(), 7: CCImunity(), 8: DoNothing()}
        self.respective_abilities = {"blindingrage": self.blinding_rage, "discourage": self.discourage, "focus": self.focus,
                                     "cleansedot": self.cleanse_DOT, "truedamage": self.true_damage, "ccimunity": self.cc_immunity}
        self._ability_list = [Taunt(), Bolster(), Strengthen()]
        self._gold = 0

    def find_nonempty_position_in_inventory(self):
        for index in range(len(self.__inventory)):
            if self.__inventory[index] is None:
                return index
        return -1

    def get_inventory(self):
        return self.__inventory

    def pick_up(self, item):
        index = self.find_nonempty_position_in_inventory()
        if index == -1:
            raise PickingError("Cannot pick up, inventory full")
        self.__inventory[index] = item

    def find_inventory_by_name(self, item_name):
        if item_name == "NoneType":
            return -1
        for index in range(len(self.__inventory)):
            if type(self.__inventory[index]).__name__.lower().strip() == item_name.lower().strip():
                return index
        return -1

    def drop_item(self, item_name):
        item_index = self.find_inventory_by_name(item_name)
        if item_index == -1:
            raise ItemError("Invalid Item!")
        item = self.__inventory[item_index]
        string = type(item).__name__ + " has been dropped!\n"
        self.__inventory[item_index] = None
        return string

    def move_weapon_to_inventory(self):
        position = self.find_nonempty_position_in_inventory()
        if position == -1:
            raise DroppingError("Inventory is full!\n")
        if type(self._weapon).__name__ == "NoWeapon":
            raise DroppingError("You have no weapon to drop!\n")
        self.__inventory[position] = self._weapon
        self._weapon = NoWeapon()

    def move_armour_to_inventory(self):
        position = self.find_nonempty_position_in_inventory()
        if position == -1:
            raise DroppingError("Inventory is full!")
        if type(self._armor).__name__ == "NoArmour":
            raise DroppingError("You have no armour to drop!\n")
        self.__inventory[position] = self._armor
        self._armor = NoArmour()

    def use_item(self, item_name):
        item_index = self.find_inventory_by_name(item_name)
        if item_index == -1:
            raise ItemError("Invalid Item!")
        item = self.__inventory[item_index]
        string = ""
        if isinstance(item, Weapon):
            string += "You have equipped " + type(self.__inventory[item_index]).__name__ + "!\n"
            old_weapon = self.change_weapon(item)
            if type(old_weapon).__name__ != "NoWeapon":
                self.__inventory[item_index] = old_weapon
            else:
                self.__inventory[item_index] = None
            self.re_set_attack_health()

        if isinstance(item, Armour):
            string += "You have equipped " + type(self.__inventory[item_index]).__name__ + "!\n"
            old_armour = self.change_armour(item)
            if type(old_armour).__name__ != "NoArmour":
                self.__inventory[item_index] = old_armour
            else:
                self.__inventory[item_index] = None
            self.re_set_attack_health()

        if isinstance(item, Potion):
            string += "You have consumed a " + type(self.__inventory[item_index]).__name__ + "!\n"
            self.__inventory[item_index] = None
            string += item.use(self)

        return string

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

    def blinding_rage(self,  opponent, list_of_turns, turn_counter):
        ability = BlindingRage()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def discourage(self, opponent, list_of_turns, turn_counter):
        ability = Discourage()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def focus(self, opponent, list_of_turns, turn_counter):
        ability = Focus()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def cleanse_DOT(self, opponent, list_of_turns, turn_counter):
        ability = CleanseDOT()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def true_damage(self, opponent, list_of_turns, turn_counter):
        ability = TrueDamage()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def cc_immunity(self, opponent, list_of_turns, turn_counter):
        ability = CCImunity()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def level_up(self):
        self.__level += 1
        self._health += 15
        self._max_health += 15
        self._innate_defense += 10
        self._innate_attack += 3
        self.re_set_attack_health()
        self.new_ability()

    def new_ability(self):
        ability_to_learn = self.abilities_to_learn[self.__level]
        ability = type(ability_to_learn).__name__
        ability = ability.lower()
        effect = self.respective_abilities[ability]
        string = self.learn_ability(ability, effect)
        self._ability_list.append(ability_to_learn)
        print(string)

    def get_level(self):
        return self.__level

    def print_inventory(self):
        table = texttable.Texttable()
        table.add_row(["Inventory:"])
        for i in range(len(self.__inventory)):
            line = list()
            if self.__inventory[i] is None:
                line.append("Empty Place\n")
            else:
                line.append(str(self.__inventory[i]))
            table.add_row(line)
        return table.draw()

    def set_up(self, name, attack, defense, weapon, armour, health, max_health, level, gold, inventory):
        self._name = name
        self._innate_attack = attack
        self._innate_defense = defense
        self._weapon = weapon
        self._armor = armour
        self._health = health
        self.__level = level
        self.__inventory = inventory
        self.re_set_attack_health()
        self._max_health = max_health
        self._gold = gold

    def learn_ability(self, ability_name, ability_efect):
        self.add_ability(ability_name, ability_efect)
        string = str(ability_name) + " has been learnt!\n"
        return string

    def cheat_to_level(self, level):
        for index in range(level - 1):
            self.level_up()

    def print_lvl(self):
        print(self.__level)

    def print_abilities_description(self):
        for ability in self._ability_list:
            print(type(ability).__name__, ":", ability.get_description())

    def gain_gold(self, amount):
        self._gold += amount

    def get_gold(self):
        return self._gold

    def buy_item(self, cost, item):
        if self._gold <= cost:
            raise ShoppingError("Not Enough Gold To Buy Item!\n")
        self.pick_up(item)
        self._gold -= cost

    def sell_item(self, cost, item):
        for index in range (len(self.__inventory)):
            if type(self.__inventory[index]).__name__.lower() == item:
                self.__inventory[index] = None
                self._gold += cost
                return True
        raise ShoppingError("Item Cannot Be Found In The Inventory!\n")

    def print_stats(self):
        string = str(self._name) + ": " + str(self._health) + " HEALTH, " + str(self._defense) + " DEFENSE, " + str(self._attack) + " ATTACK, " + str(self._gold) + " GOLD, " + str(self.__level) + " LEVEL\n"
        string += str(self._weapon)
        string += str(self._armor)
        return string

    def create_character_copy(self,  new_name, description):
        Chara = Character(new_name, self._innate_attack, self._innate_defense, self._weapon, self._armor, self._health, description)
        return Chara