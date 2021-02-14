from Characters.FinalBoss import FinalBoss
from Items.Weapons.Weapon import Weapon



class OrbOfTheTitans(Weapon):
    def __init__(self):
        super().__init__(1000, 1000)
        self.set_effect()

    def effect(self, damage, caster, opponent):
        string = ""
        if isinstance(opponent, FinalBoss):
            ratio = opponent.get_max_hp() / caster.get_max_hp()
            attack = caster.get_attack_value()
            caster.increase_attack_value(0.15 * ratio * attack)
            string = "Your attack was increased by " + str(0.15 * ratio * attack) + "!\n"
            caster.increase_armour_pen(0.3)
            string += "The power of the titans activates!\n"
            string += "Your armour pen was increased by 30%!\n"
        return string
