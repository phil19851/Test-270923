#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import pandas as pd
os.chdir("C:\Challenge\PyPoll\Resources")

# Load the CSV file into a DataFrame
election_data = pd.read_csv("election_data.csv")

# Calculate the total number of votes cast
total_votes = len(election_data)

# Create a DataFrame to store the vote counts for each candidate
candidate_votes = election_data["Candidate"].value_counts().reset_index()
candidate_votes.columns = ["Candidate", "Vote Count"]

# Calculate the percentage of votes each candidate won
candidate_votes["Percentage"] = (candidate_votes["Vote Count"] / total_votes) * 100

# Sort the candidates alphabetically
candidate_votes = candidate_votes.sort_values(by="Candidate")

# Find the winner based on popular vote
winner = candidate_votes.loc[candidate_votes["Vote Count"].idxmax()]

# Define the file name for the results
output_file = "election_results.txt"

# Open the file for writing and print the analysis
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    # Print the list of candidates and their respective vote percentages and counts
    for _, row in candidate_votes.iterrows():
        file.write(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Vote Count']})\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner['Candidate']}\n")
    file.write("-------------------------\n")

# Print the analysis to the terminal
with open(output_file, "r") as file:
    analysis = file.read()
    print(analysis)


# In[ ]:




