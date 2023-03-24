from employee import Employee
from customer import Customer

employee1 = Employee("John", "Smith", 1234)
employee2 = Employee("Jane", "Doe", 5678)
employee2.employee_id = 9874
employee2.last_name = "Smith"
customer1 = Customer("Jack", "Smith", "Cereal")
customer1.shopping = "Bowl"
customer2 = Customer("Jill", "Smith", "Milk")
customer2.shopping = "Spoon"

print(employee1)
print(employee2)
print(customer1)
print(customer2)
