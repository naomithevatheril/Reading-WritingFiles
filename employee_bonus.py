import csv

employees = open('EmployeePay.csv', 'r')

csv_file = csv.reader(employees)

for record in csv_file:
    print(f'First Name: {record[1]}')
    print(f'Last Name: {record[2]}')
    print(f'Salary: ${record[3]}') #need to make this a string
   
    #comhine record 3 with record 4 to make bonus
    #record 3 + bonus = total
    #need to figure out how to make the program pause
