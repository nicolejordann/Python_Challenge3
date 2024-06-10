

import csv
from collections import Counter


# retrieve csv data
csvpath = "Resources/election_data.csv"

#define Variables
total = 0
canvotes = Counter()

#read csv
with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header
    csv_header = next(csvreader)
    

    # Loop to count each vote for each candidate
    for row in csvreader:
        total += 1
        canvotes[row[2]] += 1
        
# formula to find the winner
winner = max(canvotes, key=canvotes.get)


# Utilizing a string to display the analysis without knowing who the winner will be
analysis = "Election Results \n" + "-----------------------\n"
analysis += "Total votes: " + str(total) + "\n"
analysis += "-----------------------\n"

#using the directory to calculate values
for candidate, votes in canvotes.items():
    percentage = (votes / total) * 100
    analysis += (str(candidate) + ": " + '{:.3f}'.format(percentage) + "% " + str(votes) + "\n")

analysis += "-----------------------\n"
analysis += "Winner: " + str(winner) + "\n"
analysis += "-----------------------\n"

#create a text file displaying the analysis
with open("Analysis/Poll_analysis.txt", "w") as txtfile:
    txtfile.write(analysis)
    