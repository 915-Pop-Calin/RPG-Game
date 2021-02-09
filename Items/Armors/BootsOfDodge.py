from Items.Armors.Armour import Armour


class BootsOfDodge(Armour):
    def __init__(self):
        super().__init__(0, 0)
        self.set_dodge(0.30)

    def get_id(self):
        return 304