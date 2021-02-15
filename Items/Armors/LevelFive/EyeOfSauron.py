from Items.Armors.Armour import Armour


class EyeOfSauron(Armour):
    def __init__(self):
        super().__init__(0, 200)
        self._description = "Super strong armour with no drawbacks.\n"

    def get_id(self):
        return 306