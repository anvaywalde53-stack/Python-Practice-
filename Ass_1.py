class Employee:
    def __init__(self, name, emp_id, dept, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.basic_salary = basic_salary

    def generate_salary_slip(self):
        da = self.basic_salary * 0.92
        hra = self.basic_salary * 0.58
        ta = self.basic_salary * 0.30
        lic = 500
        
        gross_salary = self.basic_salary + da + hra + ta
        net_salary = gross_salary - lic

        print("-" * 30)
        print(f"Salary Slip for: {self.name}")
        print(f"ID: {self.emp_id} | Dept: {self.dept}")
        print("-" * 30)
        print(f"Basic Salary: {self.basic_salary}")
        print(f"DA: {da}")
        print(f"HRA: {hra}")
        print(f"TA: {ta}")
        print(f"LIC Deduction: {lic}")
        print("-" * 30)
        print(f"Gross Salary: {gross_salary}")
        print(f"Net Salary: {net_salary}")
        print("-" * 30)

name = input("Enter Name: ")
eid = input("Enter ID: ")
dept = input("Enter Dept: ")
basic = float(input("Enter Basic Salary: "))

emp = Employee(name, eid, dept, basic)
emp.generate_salary_slip()
