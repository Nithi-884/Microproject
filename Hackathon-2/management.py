import json
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        print(f" Name: {self.name}")
        print(f" Age: {self.age}")
        print(f" Gender: {self.gender}")

class Employee(Person):
    def __init__(self, name, age, gender,emp_id,department,salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
    
    def get_details(self):
        
        print(f" Employee id: {self.emp_id}")
        super().get_details()
        print(f" Department: {self.department}")
        print(f" Salary: {self.salary}")

    def is_eligible_for_bonus(self): # return True if salary < 50000
        if self.salary < 50000:
            print(f"{self.name} is eligible for the salary.")
    
    # from_string(cls, data_string) 
# Format: "John,35,Male,E101,HR,45000"
    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, age, gender, emp_id, department, int(salary))
    # staƟc method: bonus_policy() – print bonus policy descripƟon
    @staticmethod
    def bonus_policy():
        print("The bonus is available to all employees whose salary is less than 50000")


class Department:
    def __init__(self,name,employee_list):
        self.name = name
        self.employee_list = employee_list

     # Check if the object is an instance of Student
    def add_employee(self,employee):
        if isinstance(employee, Employee): 
            self.employee_list.append(employee)
        
    def get_average_salary(self):
        if not self.employee_list:
            return 0  # Avoid division by zero
        return sum(emp.salary for emp in self.employee_list) / len(self.employee_list)  

    
    def display_employees(self):
        
        for emp in self.employees_list:
            print(emp)

def save_to_json(employees, json_path ):
    employees_data = []
   
    for emp in employees:
        emp_dict = {
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        }
        employees_data.append(emp_dict)
 
    with open(json_path, 'w') as file:
        json.dump(employees_data, file, indent=4)

    
def load_from_json(json_path):
    with open(json_path, 'r') as file:
        data_of_employees = json.load(file)
        employees = []
       
        for emp in data_of_employees:
            employees.append(Employee(
                emp["name"],
                emp["age"],
                emp["gender"],
                emp["emp_id"],
                emp["department"],
                emp["salary"]
            ))
           
        return employees


        




        