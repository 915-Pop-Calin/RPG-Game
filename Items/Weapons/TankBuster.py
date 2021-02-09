from Items.Weapons.Weapon import Weapon


class TankBuster(Weapon):
    def __init__(self):
        super().__init__(30, 0)
        self.set_effect()

    def effect(self, damage, caster, opponent):
        caster.deal_damage(opponent, damage)
        string = caster.get_name() + " did a double hit and dealt " + str(damage) + " damage!"
        return string

    def get_id(self):
        return 207

