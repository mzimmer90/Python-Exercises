from flying_animal import FlyingAnimal


class NonBirdFlyingAnimal(FlyingAnimal):
    _all_instances = []

    def __init__(self, name, wingspan, distance):
        super().__init__(name, wingspan)
        self._distance = distance
        NonBirdFlyingAnimal._all_instances.append(self)

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        self._distance = distance

    def __str__(self):
        return f"My Non-Bird Flying Animal {self.name} has a wingspan of {self.wingspan} and can fly up to " \
               f"{self.distance} miles."

    @classmethod
    def animal_with_longest_distance(cls):
        longest_distance_instance = None
        for instance in cls._all_instances:
            if longest_distance_instance is None or instance.distance > longest_distance_instance.distance:
                longest_distance_instance = instance
        return f"The Non-Bird Flying Animal with the longest distance is {longest_distance_instance.name} " \
               f"with a distance of {longest_distance_instance.distance} meters."
