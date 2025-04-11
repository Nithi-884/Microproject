

from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []
     # Add a new employee to the list
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        return employee

    # Get employee list
    def get_all_employees(self):
        return self.employees

    # Find employee by id
    def find_by_id(self, employee_id):
        return next((e for e in self.employees if e.id == employee_id), None)

    # Del employee
    def delete_employee(self, employee_id):
        employee = self.find_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(d) for d in employee_dicts]
        
    #  employee objects to list of dicts
    def to_dict_list(self):
        return [e.to_dict() for e in self.employees]
