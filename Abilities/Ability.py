class Ability:
    """
    This class will be inherited by ALL abilities in the game, so we don't have to redefine get_description for each of them.
    In this case, description is the only thing abilities share.
    """
    def __init__(self):
        """
        Description is a string of characters whose scope is to make the human player understand better what their abilities do and what
        his opponent's abilities do.
        """
        self._description = None

    def get_description(self):
        return self._description