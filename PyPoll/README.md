PyPoll Analysis:

In this analysis, we are extracting data from polling information to find the winner of an election, along with the number of votes and percentage of votes each candidate received.

First we import the csv and set the pathway to the file.
Then we set the variables we'll be using.
We'll open the csv with a dicitonary reader as we'll be using dictionaries throughout our analysis.
As we run through the rows, we will be adding a vote per row to the total vote count, adding the candidate name to a candidate list if it isn't already in the list, and adding up the votes for each individual candidate.

Our eventual voter output is going to be as a string

Then to find the percentage of the vote that each candidate received, we are looping through the number of votes each candidate received and dividing that by the total number of votes.

The winner is the person whose individual votes is the largest, as created by adding the largest number of votes to the winning count variable if it's larger than the value that was already there. Then we'll add that candidate's name to the winning candidate variable.

We're setting the voter output as a variable that will add each candidate and their vote percentage and number of votes.
Then we want to write to a new text file and print to the terminal the Election results which includes the total number of votes and each candidate's total number of votes and percentage of the total vote and finally the winning candidate.
    
