class Animal:
    def __init__(self, name):
        self._name = name
        self._tricklist = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def add_trick(self, trick):
        self._tricklist.append(trick)

    def get_tricks(self):
        return ", ".join(self._tricklist)

    def add_type(self, type):
        self._type = type

    def get_type(self):
        return self._type

    def add_breed(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

    def __str__(self):
        return f"My {self.get_type()} {self.get_name()}, who is a {self.get_breed()}, can do these tricks: {self.get_tricks()}."


class FlyingAnimal(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self._wingspan = wingspan

