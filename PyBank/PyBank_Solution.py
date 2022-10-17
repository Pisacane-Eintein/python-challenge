
import os
import csv

budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

total_months = []
list = []
profits = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
              
        total_months.append(row[0])
        list.append(row[0])
        profits.append(int(row[1]))
  
    total_months = len(total_months) 
    total_profits = sum(profits)

with open(budget_csv, "r") as f:
    lines = f.readlines()
data = []
index = {}


# Don't read the header row. Erase the newline character from each line 
# Split the line using a comma delimter. 
for line in lines[1:]: 
    line = line.strip("\n")
    data.append(line.split(","))

# Start with the second element that be subtrcted from the first
output = []
for index,element in enumerate(data[1:]):
    output.append(int(element[1])-int(data[index][1]))

average = round(sum(output)/len(output),2)
max_value = max(output)
max_index = output.index(max_value) 
max_index_adj = max_index + 1

min_value = min(output)
min_index = output.index(min_value)
min_index_adj = min_index + 1


    # Add summary table intro headers to column 0
for row in range(0,1):
    print('')
    print('Financial Analysis') 
    print('')
    print('---------------------------')
    print('')
    print(f'Total Months:  {total_months}')
    print('')
    print(f'Total: ${total_profits} ')
    print('')
    print(f'Average Change: ${average}')
    print('')
    print(f'Greatest Increase in Profits: {list[max_index_adj]} $({max_value})  ')
    print('')
    print(f'Greatest Decrease in Profits: {list[min_index_adj]} $({min_value})  ')


# write to a new csv file
with open('Analysis/budget_output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')

     # Add summary table intro headers to column 0
    for row in range(0,1):
 
        writer.writerow(['Financial Analysis']) 
        writer.writerow(['---------------------------'])
        writer.writerow([f'Total Months:  {total_months}'])
        writer.writerow([f'Total: {total_profits} '])
        writer.writerow([f'Average Change: {average}'])
        writer.writerow([f'Greatest Increase in Profits: {list[max_index_adj]} $({max_value})  '])
        writer.writerow([f'Greatest Decrease in Profits: {list[min_index_adj]} $({min_value})  '])
    