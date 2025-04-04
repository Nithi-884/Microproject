from management import Employee, Department,save_to_json,load_from_json
# -----------------------
# Sample Main Execution
# -----------------------

data_strings = [
    "Alice,30,Female,E101,HR,48000",
    "Bob,28,Male,E102,IT,55000",
    "Charlie,35,Male,E103,HR,60000",
    "Diana,26,Female,E104,IT,47000",
    "Evan,40,Male,E105,Finance,53000"
]

# Create Employee objects
employees = [Employee.from_string(s) for s in data_strings]
# print(employees)

# Create Departments and assign employees
departments = {}
for emp in employees:
    if emp.department not in departments:
        departments[emp.department] = Department(emp.department,[])
    departments[emp.department].add_employee(emp)

# print(departments)
# Print Details
Employee.bonus_policy()
print("\nEmployee Details:")
for emp in employees:
    print(emp.get_details())

# Print Department Average Salaries
print("\nAverage Salaries by Department:")
for dept_name, dept in departments.items():
    print(f"{dept_name}: ₹{dept.get_average_salary():.2f}")

# Save Data
save_to_json(employees,json_path = r"C:\Users\292905\Desktop\Python semicon\Hackathon-2\employee.json" )

# Load and verify
print("\n📂 Loaded Data from JSON:")
loaded_emps = load_from_json(json_path=r"C:\Users\292905\Desktop\Python semicon\Hackathon-2\employee.json")
for emp in loaded_emps:
    print(emp.get_details())
