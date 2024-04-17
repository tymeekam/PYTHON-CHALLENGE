#module allows us to find the working directory/file path
import os

#module will allow reading of CSV files
import csv

#create a variable (csvpath) that holds the location of the file
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

#tell it to locate that 
print(csvpath)

#see what type of datatype it is
print(type(csvpath))



#open the CSV as a CSV file
with open(csvpath) as csvfile:
 #do the same thing with the CSV reader & tell it how the info is separated
    csvreader = csv.reader(csvfile, delimiter=',')

    #store headers & RUN IT AS A LIST
    csv_header = next(csvreader)
    print(f'CSV HEADERS: {csv_header}')
   #create a loop to pull out data from csv reader variable
    for row in csvreader:
        print(row)
        
    #total_months = 0
    #total = 0
    #for row in reader:
        #total_months = total_months + 1
      
    #print(f"Total Months: {total_months}")
    #print(f"total: ${total}")
