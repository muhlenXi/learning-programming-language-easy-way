from PersonEx.Employee import Employee
from PersonEx.Person import Person


mars = Employee(11, "mars", 30)
eleven = Employee(11, "mars", 30)

print(Employee._Employee__counter)

print(mars)
print(issubclass(Employee, Person))

print(isinstance(mars, Person))
print(isinstance(mars, Employee))

print(mars.__repr__())
print(mars.__str__())

print(mars == eleven)

