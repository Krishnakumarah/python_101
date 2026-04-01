def print_employee_details(employee_data):
    # Write code here
    if not employee_data:
        print("No data available")
        return

    for key,value in employee_data.items():
            print(f'{key}: {value}')
staff_info = {
   
}
print_employee_details(staff_info)
