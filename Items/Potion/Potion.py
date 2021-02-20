class Potion:
    def __init__(self):
        self._description = None

    def __str__(self):
        string = type(self).__name__ + ": " + self._description
        return string