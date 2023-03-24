from person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self._employee_id = employee_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Employee ID is: {self.employee_id}"
