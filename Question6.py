class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_salary(self):
        print(f"{self.name}'s salary is calculated based on a base salary of {self.base_salary}.")
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus
        print(
            f"{self.name}'s total salary as a manager is {total_salary} (Base Salary: {self.base_salary} + Bonus: {self.bonus}).")
employee = Employee("Emmanuel", 45000)
employee.calculate_salary()
manager = Manager("Lydia", 55000, 15000)
manager.calculate_salary()
