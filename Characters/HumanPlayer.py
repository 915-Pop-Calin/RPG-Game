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
from Exceptions.exceptions import PickingError, ItemError, ShoppingError, LoadingError
from Items.Armors.Armour import Armour
from Items.Armors.LevelOne.Bandage import WornBandage
from Items.Potion.Potion import Potion
from Items.Weapons.LevelOne.ToyKnife import ToyKnife
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
                                     "cleansedot": self.cleanse_DOT, "truedamage": self.true_damage, "ccimunity": self.cc_immunity,
                                     "donothing": self.donothing}
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


    def use_item(self, item_name):
        item_index = self.find_inventory_by_name(item_name)
        if item_index == -1:
            raise ItemError("Invalid Item!")
        item = self.__inventory[item_index]
        string = ""
        if isinstance(item, Weapon):
            string += "You have equipped " + type(self.__inventory[item_index]).__name__ + "!\n"
            old_weapon = self.change_weapon(item)
            self.__inventory[item_index] = old_weapon
            self.re_set_attack_health()

        if isinstance(item, Armour):
            string += "You have equipped " + type(self.__inventory[item_index]).__name__ + "!\n"
            old_armour = self.change_armour(item)
            self.__inventory[item_index] = old_armour
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

    def donothing(self, opponent, list_of_turns, turn_counter):
        ability = DoNothing()
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
        string = ""
        for element in self.__inventory:
            if element == None:
                string += "Empty Place\n"
            else:
                string += str(element)
                string += "\n"
        return string

    def set_up(self, name, attack, defense, weapon, armour, health, level, gold, inventory):
        self._name = name
        self._innate_attack = attack
        self._innate_defense = defense
        self._weapon = weapon
        self._armor = armour
        self._health = health
        self.__level = level
        self.__inventory = inventory
        self.re_set_attack_health()
        self._max_health += 5 * self.__level
        self._gold = gold

    def save_level_and_status(self, level, filename):
        saved_level = level
        name = self._name
        attack = self._innate_attack
        defense = self._innate_defense
        weapon = self._weapon.get_id()
        level_player = self.__level
        armour = self._armor.get_id()
        health = self._health
        gold = self._gold
        inventory = []
        for element in self.__inventory:
            if element is None:
                inventory.append(0)
            else:
                inventory.append(element.get_id())

        with open(filename, 'w') as file:
            line = str(saved_level) + ";" + str(name) + ";" + str(attack) + ";" + str(defense) + ";" + str(weapon) + ";" + str(armour) + ";" + str(health) + ";" + str(level_player) + ";" + str(gold) + ";"
            for index in range (len(inventory)):
                line += str(inventory[index])
                if index != len(inventory) - 1:
                    line += ";"
            line += "\n"
            file.write(line)

    def load_save_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                raise LoadingError("No save file to load!\n")
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
            gold = int(line[8])
            inventory = []
        for index in range(9, 17):
            if int(line[index]) == 0:
                inventory.append(None)
            else:
                inventory.append(self.ids[int(line[index])]())
        for index in range (2, saved_level + 1):
            classname = self.abilities_to_learn[index]
            self._ability_list.append(classname)
            classname = type(classname).__name__
            classname = classname.lower()
            self.add_ability(classname, self.respective_abilities[classname])
        self.set_up(name, attack, defense, weapon, armour, health, level, gold, inventory)
        selves = [None,None,None]
        current_self = 0
        for index in range(1, len(lines)):
            if lines[index] != "\n":
                chara = self.load_character(filename, index)
                selves[current_self] = chara
                current_self += 1
        return saved_level, selves

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