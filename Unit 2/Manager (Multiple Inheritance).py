# Create python program to show how the manager class inherits attributes and methods from both Person and Employee
# and how we can add additional behaviors and properties in the Manager Class. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

def work(self):
        return f"Employee {self.employee_id} is now logging hours."

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Pass details to the Employee class
        super().__init__(name, age, employee_id, salary)
        # New property unique to Manager
        self.department = department
        self.team = []

    # Additional behavior: Managing a team
    def add_subordinate(self, employee_name):
        self.team.append(employee_name)
        return f"{employee_name} has been added to {self.name}'s team."

    def conduct_meeting(self):
        return f"Manager {self.name} is holding a meeting for the {self.department} department."

    # Overriding a method to add more detail
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I manage the {self.department} team."

# --- Demonstration ---
mgr = Manager("ABC", 19, "ABC1000", 950000, "CSE")

print(mgr.introduce())   
print(mgr.work())              
print(mgr.conduct_meeting())   
print(mgr.add_subordinate("Bob"))
