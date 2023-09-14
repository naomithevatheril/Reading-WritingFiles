#notes in class:
import csv

custid= 250
total= 0

sales = open('sales.csv', 'r')
salesreader= csv.reader(sales)
next(salesreader)

salesreport = open('salesreport.csv', 'w')
salesreport.write("Customer ID, Total \n")

for rec in salesreader:
    if custid == int(rec[0]):
        total+= float(rec[3])+float(rec[4])+float(rec[5])
    else:
        salesreport.write(f'{custid},{total:.2f}\n')
        custid+=1
        total=float(rec[3])+float(rec[4])+float(rec[5])

salesreport.close()
    
    

