from employee_manager import EmployeeManager
from storage import Storage


# Display employees to be used in the while loop
def display_employees(employees):
    if not employees:
        print("No employees found.")
    for e in employees:
        print(f"{e.id} - {e.name}, Dept: {e.department}, Role: {e.designation},Gross Salary: {e.gross_salary}, Net Salary: {e.net_salary}")

def main():
    # Initilize objects
    manager = EmployeeManager()
    storage = Storage("employees.pkl")

    saved_data = storage.load()
    manager.load_employees(saved_data)

    while True:
        print("\n1. Add Employee\n2. View All\n3. Search by ID\n4. Delete Employee\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            dept = input("Department: ")
            role = input("Designation: ")
            gross = float(input("Gross Salary: "))
            tax = float(input("Tax: "))
            bonus = float(input("Bonus: "))

            emp = manager.add_employee(name, dept, role, gross, tax, bonus)
            storage.save(manager.to_dict_list())
            print(f"Employee added with ID: {emp.id}")

        elif choice == '2':
            display_employees(manager.get_all_employees())

        elif choice == '3':
            eid = input("Enter employee ID: ")
            emp = manager.find_by_id(eid)
            if emp:
                print(f"{emp.id} - {emp.name}, Dept: {emp.department}, Role: {emp.designation}, Net Salary: {emp.net_salary}")
            else:
                print("Employee not found.")

        elif choice == '4':
            eid = input("Enter employee ID: ")
            if manager.delete_employee(eid):
                storage.save(manager.to_dict_list())
                print("Employee deleted.")
            else:
                print("Employee not found.")

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
