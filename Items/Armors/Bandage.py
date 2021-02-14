from Items.Armors.Armour import Armour


class WornBandage(Armour):
    def __init__(self):
        super().__init__(0, 3)
        self._description = "Bandaid Solution for beginners.\n"

    def get_id(self):
        return 300