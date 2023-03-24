from person import Person


class Customer(Person):
    def __init__(self, first_name, last_name, item):
        super().__init__(first_name, last_name)
        self._shopping = []
        self._shopping.append(item)

    @property
    def shopping(self):
        return ", ".join(self._shopping)

    @shopping.setter
    def shopping(self, item):
        self._shopping.append(item)

    def __str__(self):
        return f"{self.first_name} {self.last_name} has purchased these items: {self.shopping}"
