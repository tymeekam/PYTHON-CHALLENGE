#module allows us to find the working directory/file path
from datetime import date
import os

#module will allow reading of CSV files
import csv

#create a variable (csvpath) that holds the location of the file
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

total_months = 0
net_total = 0
previous_profit_value = None
changes = []
greatest_increase = 0
greatest_decrease = 0
increase_month = None
decrease_month = None

months = []
pl = []
delta = []
prev = 0

#open the CSV as a CSV file
with open(csvpath) as csvfile:

 #do the same thing with the CSV reader & tell it how the info is separated
    csvreader = csv.reader(csvfile, delimiter=',')

    # #store headers & RUN IT AS A LIST
    csv_header = next(csvreader)

    for row in csvreader:

        #print(row[1])
        months.append(row[0])
        pl.append(int(row[1]))

        if len(pl) == 1:
            prev = int(row[1])
        else:
            delta.append(int(row[1]) - prev)
            prev = int(row[1])


# AFTER THE FOR LOOP COMPLETES}
print("Financial Analysis")

print("----------------------------")

print(f'Months: {(len(months))}')
print(f'Total: ${(sum(pl))}')
print(f'Average: ${(sum(delta)/len(delta)):.2f}')
print(f'Greatest Increase in Proft: {months[delta.index(max(delta)) + 1]}  (${max(delta)})')
print(f'Greatest Decrease in Profit: {months[delta.index(min(delta)) + 1]}  (${min(delta)})')

# # Export to a text file
with open("results.txt", "w") as file:
    file.write(f'Months: {(len(months))}')
    file.write(f'Total: ${(sum(pl))}')
    file.write(f'Average: ${(sum(delta)/len(delta)):.2f}')
    file.write(f'Greatest Increase in Proft: {months[delta.index(max(delta)) + 1]}  (${max(delta)})')
    file.write(f'Greatest Decrease in Profit: {months[delta.index(min(delta)) + 1]}  (${min(delta)})')

print("Results exported to results.txt")
