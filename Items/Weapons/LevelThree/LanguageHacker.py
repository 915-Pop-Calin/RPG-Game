from Exceptions.exceptions import PickingError
from Items.Potion.GrainOfSalt import GrainOfSalt
from Items.Weapons.Weapon import Weapon


class LanguageHacker(Weapon):
    def __init__(self):
        super().__init__(10, 0)
        self.set_effect()
        self._description = "After each attack, you gain a GrainOfSalt.\n"

    def effect(self, damage, caster, opponent):
        try:
            caster.pick_up(GrainOfSalt())
            string = "Grain of Salt was added to your inventory!\n"
        except PickingError as PE:
            string = "Grain of salt was not added to your inventory because inventory was full!\n"
        return string
