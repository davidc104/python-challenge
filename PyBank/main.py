# Import os module 
import os
# Import csv module 
import csv

# Define a function to print the results
def print_results(totalMonth01, totalProfit01, totalChange01, greatGain_m01, greatGain01, greatLoss_m01, greatLoss01):
   # Display Results # 
   print('Financial Analysis')
   print('----------------------------')   
   #The total months 
   print(f'Total Months : {totalMonth01}')
   #The total amount of Profit/Losses over the entire period
   print(f'Total: ${totalProfit01}')
   #The Average change over the entire period
   print(f'Average Change: ${round(totalChange01 / (totalMonth01 - 1), 2)}')
   # Greatest increase in profits
   print(f'Greatest Increase in Profits: {greatGain_m01} (${greatGain01})')
   # Greatest Descrease in profits
   print(f'Greatest Decrease in Profits: {greatLoss_m01} (${greatLoss01})')
   
# Join the directory and the csv file to form the file path
csvpath = os.path.join('Resources','budget_data.csv')

# Declare variables
firstRow = True
currDate = 0
currProfit = 0
preProfit = 0
gainLoss = 0
greatGain = 0
greatGain_m = 0
greatLoss = 0
greatLoss_m = 0
totalChange = 0
totalMonth = 0
totalProfit = 0

#Open and read CSV file
with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')

   # Read the header row first
   csv_header = next(csvreader)
   
   # Read each row of data after the header
   for row in csvreader:
      currDate = row[0]
      currProfit = int(row[1])
      gainLoss =  currProfit - preProfit

      if firstRow == True:
         firstRow = False
      else:   
         totalChange += gainLoss
      
      # Compare gainLoss with greatGain or with greatLoss to determine gain or loss
      if gainLoss >  greatGain:
            greatGain = gainLoss
            greatGain_m = currDate
      elif gainLoss <  greatLoss:
            greatLoss = gainLoss
            greatLoss_m = currDate
      
      # Re-assign previous profit for the next run
      preProfit = currProfit   
      
      # Increase total month 
      totalMonth += 1

      # Increase total profit   
      totalProfit += currProfit 
      
print_results(totalMonth, totalProfit, totalChange, greatGain_m, greatGain, greatLoss_m, greatLoss)

# Export a text file with the results 
with open('Financial_Analysis.txt', 'w') as txtwriter:
   txtwriter.write("Financial Analysis" + "\n")
   txtwriter.write("----------------------------"  + "\n")
   txtwriter.write(f"Total Months: {totalMonth}"  + "\n")
   txtwriter.write(f"Total: ${totalProfit}"  + "\n")
   txtwriter.write(f"Average Change: {round(totalChange / (totalMonth - 1), 2)}"  + "\n")
   txtwriter.write(f"Greatest Increase in Profits: {greatGain_m} (${greatGain})"  + "\n")
   txtwriter.write(f"Greatest Decrease in Profits: {greatLoss_m} (${greatLoss})"  + "\n")
