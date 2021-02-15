from Items.Armors.Armour import Armour


class Scales(Armour):
    def __init__(self):
        super().__init__(0, 20)
        self._description = "Scales of Chtulhu. Does not serve as very good armour.\n"

    def get_id(self):
        return 305