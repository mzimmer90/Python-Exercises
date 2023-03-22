class Animal:
    def __init__(self, name):
        self._name = name
        self._tricklist = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tricks(self):
        return ", ".join(self._tricklist)

    @tricks.setter
    def tricks(self, trick):
        self._tricklist.append(trick)

    def add_type(self, type):
        self._type = type

    def get_type(self):
        return self._type

    def add_breed(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

    def __str__(self):
        return f"My {self.get_type()} {self.name}, who is a {self.get_breed()}, can do these tricks: {self.tricks}."


