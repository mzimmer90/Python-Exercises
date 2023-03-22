from animal import Animal

class FlyingAnimal(Animal):

    flying_animal_count = 0

    def __init__(self, name, wingspan):
        super().__init__(name)
        self._wingspan = wingspan
        FlyingAnimal.flying_animal_count += 1

    def __str__(self):
        return f"My {self.get_type()} {self.name} has a wingspan of {self._wingspan}."

    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, wingspan):
        self._wingspan = wingspan

