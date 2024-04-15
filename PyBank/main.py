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
    change = 0

    #read header row
    csv_header = next(csvreader)

    #read through each row of csv file
    for row in csvreader:
        
        #increment month count by 1
        total_months += 1
        
        #add profit/loss to total
        total = total + int(row[1])

        #start totaling and tracking change after first row
        if prev_row != 0:

            change = int(row[1]) - prev_row

            total_change += change

        #tracking greatest increase in profit
        if change > greatest_profit:
            greatest_profit = change
            profit_month = row[0]

        #tracking greatest decrease in profit
        elif change < greatest_loss:
            greatest_loss = change
            loss_month = row[0]

        #setting current row to prev_row for next row calculations
        prev_row = int(row[1])

#calculated average change
avg_change = round(total_change / (total_months - 1), 2)

#print financial analysis summary to terminal
print("Financial Analysis",)
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {loss_month}  (${greatest_loss})")

#print financial analysis summary to .txt file
os.chdir('Analysis')
with open("output.txt", "a") as f:

    print("Financial Analysis", file=f)
    print("------------------------------", file=f)
    print(f"Total Months: {total_months}", file=f)
    print(f"Total: ${total}", file=f)
    print(f"Average Change: ${avg_change}", file=f)
    print(f"Greatest Increase in Profits: {profit_month} (${greatest_profit})", file=f)
    print(f"Greatest Decrease in Profits: {loss_month}  (${greatest_loss})", file=f)


