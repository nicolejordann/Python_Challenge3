
import csv

#retrieve CSV data
csvpath = "Resources/budget_data.csv"

#define variables
profits = []
highestdate = "date"
lowestdate = "date"
highestnum = 0
lowestnum = 0


#read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
#skip header
    csv_header = next(csvreader)

#loop for obtaining data        
    for row in csvreader:
        #create a list better analyze numerical data (probs not necessary but I couldn't figure it out the other way)
        profits.append(int(row[1]))

        # conditions to find highest and lowest numbers and their respective dates
        if int(highestnum) < float(row[1]):
            highestnum = row[1] 
            highestdate = row[0]

        if int(lowestnum) > float(row[1]):
            lowestnum = row[1]
            lowestdate = row[0]

#formulas for data analysis
    n = len(profits)
    average = sum(profits) / n
    total = sum(profits)
    months = len(profits)

#utilizing a string to write analysis
analysis = "Financial Analysis\n"
analysis += "-----------------------\n"
analysis += "Total Months: " + str(months) + "\n"
analysis += "Total: $" + str(total) + "\n"
analysis += "Average Change: " + str(average) + "\n"
analysis += "Greatest Increase in Profits: " + highestdate + " ($" + str(highestnum) + ")\n"
analysis += "Greatest Decrease in Profits: " + lowestdate + " ($" + str(lowestnum) + ")\n"

#create a txt file from analysis
with open("Analysis/budget_analysis.txt", "w") as txtfile:
    txtfile.write(analysis)