import csv

employees = open('EmployeePay.csv', 'r')

csv_file = csv.reader(employees)

next(csv_file)

for record in csv_file:
    print(f'First Name: {record[1]}')
    print(f'Last Name: {record[2]}')
    print(f'Salary: ${int(record[3]):10,.2f}')
    print(f'Bonus: ${float(record[3])*float(record[4]):10,.2f}')
    total= float(record[3])+(float(record[3])*float(record[4]))
    print(f'Total: ${total:10,.2f}')

    input("Press enter to continue:") 
    
