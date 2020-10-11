import os
import csv

#find path
file_to_load = os.path.join("Resources", "budget_data.csv")

#open file
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

 #variables
    month_count = []
    profit = []
    change_profit = []
    
 #total month                    
    for row in csvreader:
        month_count.append(row[0])
              profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      

increase = max(change_profit)
month_max_increase = change_profit.index(max(change_profit))+1

decrease = min(change_profit)
month_max_decrease = change_profit.index(min(change_profit))+1

#print
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_max_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_max_decrease]} (${(str(decrease))})")      

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_max_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_max_decrease]} (${(str(decrease))})")
