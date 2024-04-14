#Modules
import os 
import csv

#Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Set all varibles to be tracked to 0
    total_months = 0
    total = 0
    greatest_profit = 0
    greatest_loss = 0
    prev_row = 0
    total_change = 0

    #read header row
    csv_header = next(csvreader)

    #read through each row of csv file
    for row in csvreader:
        
        #increment month count by 1
        total_months += 1
        
        #add profit/loss to total
        total = total + int(row[1])

        change = int(row[1]) - prev_row

        total_change += change
        
        print(f"{change}           {total_change}")

        if change > greatest_profit:
            greatest_profit = change

        elif change < greatest_loss:
            greatest_loss = change

        prev_row = int(row[1])

#avg_change = round(total_change / (total_months - 1), 2)
#print(total_change)

#print("Financial Analysis")
#print("_____________________________")
#print(f"Total Months: {total_months}")
#print(f"Total: ${total}")
#print(f"Average Change: ${avg_change}")
#print(f"Greatest Increase in Profits: ${greatest_profit}")
#print(f"Greatest Decrease in Profits: ${greatest_loss}")


