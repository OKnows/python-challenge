PyBank Analysis:


    In this analysis, we are pulling data for profits/losses over a time period, and calculating various items.
    First we import the csv and set the pathway to the correct folder
    Then we set the variables, including an empty list to track the profit changes over each row
    I open the csv as a reader and skip the header.
    Then we want to go through each row, counting the months as we go to the next row and adding up the Profits and losses over the entire period represented in the data.
    We want to make sure that the first row profits are counted as the prior month's profits when it moves to the next row, so we set that value if the month=1, which it will only equal in that first row.
    Otherwise, we'll append the profit change list by the increase by month, which is the profit loss value minus the prior month's profit, and replace the prior month's profit with the row's value before moving to the next row.
    We want to make sure that the greatest increase will always be the highest increase, so we set that by saying that if the increase by month is larger than the current value of the greatest increase, then we need to place that value into the greatest increase variable. We also will then add the date in that row to the variable for the greatest increase date. That way it will track both through the data.
    We'll do the same thing for the greatest decrease, but switching it so that these values are populated if the increase by month is less than the value in the greatest decrease value. 
    Then we want to calculate the average change, which is taking the values that were added to the profit change list and dividing that number by the number of changes in the list.
    We have our output printing to both the terminal and writing to a newly created text file. This Financial Analysis includes the total months, total profits, average revenue change, greatest increase in profits-along with the date, and greatest decrease in profits-along with that date. 
    
