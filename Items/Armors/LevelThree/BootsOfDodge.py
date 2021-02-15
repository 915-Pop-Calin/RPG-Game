from Items.Armors.Armour import Armour


class BootsOfDodge(Armour):
    def __init__(self):
        super().__init__(0, 10)
        self.set_dodge(0.15)
        self._description = "Gives you a small chance of dodging autoattacks.\n"

    def get_id(self):
        return 304