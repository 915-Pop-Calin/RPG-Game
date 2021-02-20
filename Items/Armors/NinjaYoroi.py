from Items.Armors.Armour import Armour


class NinjaYoroi(Armour):
    def __init__(self):
        super().__init__(0, 0)
        self.set_dodge(0.5)
        self._description = "Armour with no defense points but gives 50% dodge chance.\n"

    def get_id(self):
        return 309