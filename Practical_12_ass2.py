import pandas as pd

def employee_reports():
    try:
        # Load the Excel file
        file_path = 'employee.xlsx'
        df = pd.read_excel(file_path)

        # a) Print the list of employees working for "Automotive" domain
        print("--- Employees in Automotive Domain ---")
        automotive_emps = df[df['Department'] == 'Automotive']
        print(automotive_emps)

        # b) Print details of an employee with employee ID given by user
        emp_id_input = int(input("\nEnter Employee ID to search: "))
        employee_detail = df[df['Employee ID'] == emp_id_input]
        
        if not employee_detail.empty:
            print(f"\nDetails for Employee ID {emp_id_input}:")
            print(employee_detail)
        else:
            print(f"\nNo employee found with ID {emp_id_input}")

        # d) Print the list of all the Developers of Infosys
        print("\n--- List of all Developers ---")
        developers = df[df['Designation'] == 'Developer']
        print(developers)

    except FileNotFoundError:
        print("Error: The file 'employee.xlsx' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
employee_reports()
