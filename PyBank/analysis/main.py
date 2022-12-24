import os
import csv

#Set path for csv file analyze
absolute_path = os.path.dirname(__file__)
csvpath = os.path.join(absolute_path,"..", "Resources", "budget_data.csv")

#setting variables and values 
greatest_increase = 0
greatest_decrease = 0 
increase_by_month = None  
month_counter = 0  
prior_month_profit = 0   
total_profits = 0
greatest_increase_date = None
greatest_decrease_date = None
profit_change_list=[]

#Open and read the CSV
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    header = next(csv_reader)

#Creating the month counter to add 1 for each row which leads to total number of months included in the dataset
    for row in csv_reader:
        month_counter += 1
#Creating profit counter to find the net total amount of "Profit/Losses" over the entire period       
        total_profits = total_profits + int(row[1])
        
#The greatest increase in profits (date and amount) over the entire period: 
#setting it so that it will count the value in the profit/losses column for the first row for prior month profit since it's the 1st one      
        if month_counter ==1:
                prior_month_profit = float(row[1])
 #If it's not the first row, then the rows will add to the number of months
        else:   
                month = row[0]
#And the increase by month will be set to the value in the profit/loss column minus the prior month's profit            
                profit_loss = float(row[1])
                increase_by_month = profit_loss - prior_month_profit
                profit_change_list.append(increase_by_month)
        #Replace the prior month profit with the new row's profit
                prior_month_profit = float(row[1])   
   #If the increase by month is greater than the greatest increase, add the value of that increase by month to the greatest increase variable.            
                if increase_by_month > greatest_increase:
                        greatest_increase = increase_by_month
#And add the value of the date in that row to the greatest increase date variable            
                        greatest_increase_date = row[0]         
#The greatest decrease in profits (date and amount) over the entire period  
    #If the increase by month is less than the greatest increase, add the value of that increase by month to the greatest increase variable.           
                if increase_by_month < greatest_decrease:
                        greatest_decrease = increase_by_month
#And add the value of the date in that row to the greatest increase date variable            
                        greatest_decrease_date = row[0]
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #*************Do I need something else here?**********************
change_average= sum(profit_change_list)/len(profit_change_list)    
#Summarize findings
output = (f"\nFinancial Analysis\n" 
          f"---------------\n" 
          f"Total Months: {month_counter}\n" 
          f"Total Profits: ${total_profits:,.2f}\n" 
          f"Average Revenue Change: ${change_average:,.2f}\n"
          f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,.2f})\n"
          f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,.2f})\n")

#Print analysis to terminal
print(output)

#Set path for text file output
txt_outputpath = os.path.join(absolute_path, "..","Resources", "budget_analysis.txt") 
#Export analysis in text file    
with open(txt_outputpath, "w") as txt_file:
    txt_file.write(output)             