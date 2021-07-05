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

#open the elction results and read the file.
with open(file_to_load) as election_data:

    #to do: read and analyse the data here.
    file_reader = csv.reader(election_data)

    # Read and print the head row.
    headers= next(file_reader)
    print(headers)