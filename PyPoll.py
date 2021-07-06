# The data we need to retrieve
#1. The total number votes cast
#2. A complete list of Candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winnder of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis" ,  "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}

# Winning canidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the elction results and read the file.
with open(file_to_load) as election_data:

    #to do: read and analyse the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1
    
        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    # Print the Final Vote count to the terminal
    election_results = (
        f"\nElenction Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f'-------------------------\n')
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2 Retrive vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3 Calcute the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count. 

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning counts = votres and winning percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #and set the winning candidate equal to the candidate name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"----------------------------\n"
        f'Winner: {winning_candidate}\n'
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"----------------------------\n")
    print(winning_candidate_summary)

    #save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)