import os
import csv

#Set path for csv file analyze
absolute_path = os.path.dirname(__file__)
csvpath = os.path.join(absolute_path,"..", "Resources", "election_data.csv")

#Set variables
vote_counter = 0
candidate_list = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#Read csv as a list of dictionaries
with open(csvpath) as poll_data:
    reader = csv.DictReader(poll_data)

#Go through rows and add votes to vote counter
    for row in reader:
        vote_counter = vote_counter + 1

#Pull the candidate name from each row and add to the candidate list if it isn't already there
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)     
            #and start a count of votes for that candidate
            candidate_votes[candidate_name] = 0 
        #Adding a vote to their count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
 
voter_output = ""
 
 #Find vote percentages by looping through the counts
for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(vote_counter) * 100
        
        #then find the winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        #print each candidate's vote count and percentage
        voter_output += f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n"    
        print(voter_output)        
#Export data to a txt file
txt_output = os.path.join(absolute_path,"..", "analysis", "poll_analysis.txt")      
with open(txt_output, "w") as txt_file:
    
    #print vote count in terminal
    election_results = (f'\nElection Results\n' 
                        f'------------\n'
                        f'Total Votes: {vote_counter:,}\n'
                        f'------------\n'
                        f'Votes Per Candidate: {voter_output}\n'
                        f'Winning Candidate: {winning_candidate}\n')
    print(election_results)
    
    #Add final vote count to the txt file
    txt_file.write(election_results)
    
         
        