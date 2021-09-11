#The data that needs to be retrieved
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("C:\\Users\\FrantheMan\\Desktop\\Classwork\\resources\\Election_Analysis\\analysis\\election_analysis.txt")

# Initializing the vote counter
total_votes = 0

# New list to print the candidate from each row
candidate_options = []
# New list to print candidate and their votes
candidate_votes = {}

#Winning candidate and winning count tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here. 

    file_reader = csv.reader(election_data)

# Print the header row
    headers = next(file_reader)
    

# Print each row in the CSV file.
    for row in file_reader:
        total_votes+= 1
    
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
    election_results =(
        f"Election Results\n"
        f"-----------------------\n"
        f"Total Votes:{total_votes}\n"
        f"-----------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
  
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        formatted_vote_percentage = format(vote_percentage,".1f")
            
# Print out the winning candidate, vote count, and percentage

        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        if (votes > winning_count) and (vote_percentage> winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name    
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)