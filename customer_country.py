import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers)

customer_file = open('customer_country.csv', 'w')

for record in csv_file:
    customer_file.write(f'{record[1]} {record[2]}, {record[4]}')
    customer_file.write('\n')
  
customer_file.close()
customers.close()

