class Field:
    def __init__(self, new_value=""):
        self.__value = None
        self.value = new_value

    def __str__(self):
        return str(self.__value)
