'''refactor procedural code into a class-based design.
Object-Oriented principles
Encapsulation'''

salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)

# Refactored Code:
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_net_salary(self):
        tax = self.salary * 0.2
        net = self.salary - tax
        return net
# Example usage
employee = Employee(50000)
print(employee.calculate_net_salary())

