# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    def calculate_bonus(self):
        return self.salary * 0.05   # default 5% bonus


# Derived class: Manager
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # call parent constructor
        self.team_size = team_size

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"

    def calculate_bonus(self):
        # Managers get higher bonus depending on team size
        return self.salary * (0.10 + 0.01 * self.team_size)


# Derived class: Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"Developer: {self.name}, Salary: {self.salary}, Language: {self.programming_language}"

    def calculate_bonus(self):
        # Developers get a flat 8% bonus
        return self.salary * 0.08


# Derived class: Intern
class Intern(Employee):
    def __init__(self, name, salary, duration_months):
        super().__init__(name, salary)
        self.duration_months = duration_months

    def get_details(self):
        return f"Intern: {self.name}, Salary: {self.salary}, Duration: {self.duration_months} months"

    def calculate_bonus(self):
        # Interns get a fixed stipend bonus
        return 1000

employees = [
    Manager("Rajesh", 80000, 5),
    Developer("Punam", 60000, "Python"),
    Intern("Prince", 10000, 6)
]

for emp in employees:
    print(emp.get_details())
    print("Bonus:", emp.calculate_bonus())
    print("---")
