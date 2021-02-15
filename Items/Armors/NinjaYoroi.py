from Items.Armors.Armour import Armour


class NinjaYoroi(Armour):
    def __init__(self):
        super().__init__(0, 0)
        self.set_dodge(0.5)