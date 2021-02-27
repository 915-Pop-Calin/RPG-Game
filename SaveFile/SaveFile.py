import pickle
import random


class SaveFile:
    def __init__(self, number):
        self._number = number
        self._name = "SaveFile\SaveFiles\savefile" + str(number) + ".bin"

    def load_info(self):
        list_of_information = []
        try:
            with open(self._name, "rb") as file:
                list_of_information = pickle.load(file)
                file.close()
        except EOFError:
            pass
        except IOError as Error:
            raise Error
        return list_of_information

    def save_info(self, list_of_information):
        with open(self._name, "wb") as file:
            pickle.dump(list_of_information, file)
            file.close()

    def __str__(self):
        contained_info = self.load_info()
        if len(contained_info) == 0:
            return "Save File " + str(self._number) + ": Empty Save File\n"
        character = contained_info[0]
        return "Save File " + str(self._number) + ":\n" + character.print_stats()

    def delete_save_file(self):
        with open(self._name, "wb") as file:
            file.close()
