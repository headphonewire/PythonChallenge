import os, csv


PyBank_file = os.path.join("/Users/tajcu/Desktop/Python_Assignment/Starter_Code (7)/PyBank","budget_data.csv")

net_total = months_count = change = greatest_increase =  greatest_decrease = 0
greatest_increase_month = greatest_decrease_month = ("")
data = []


with open(PyBank_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    file_header = next(csvreader)

    for row in csvreader:
      
        months_count = months_count + 1
   
        net_total = int(net_total) + int(row[1])
 
        data.append(row)
        
      
        for i in range(len(data)-1):
            monthly_change = int((data)[i + 1][1]) - int((data)[i][1])

            if greatest_increase < monthly_change:
                greatest_increase = monthly_change
                greatest_increase_month = data[i + 1][0]                

            if  greatest_decrease > monthly_change:
                    greatest_decrease = monthly_change
                    greatest_decrease_month = data[i + 1][0]

            average_change = round((int((data)[-1][1]) - int((data)[0][1])) / (len(data)-1),2)

output_file = os.path.join("pybank_ result.csv")
with open(output_file,"w",newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f'Total Months: {months_count}'])
    writer.writerow([f'Total: ${net_total}'])
    writer.writerow([f'Average Change : ${average_change}'])
    writer.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'])
    writer.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})'])

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months_count}')
print(f'Total: ${net_total}')
print(f'Average Change : ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')