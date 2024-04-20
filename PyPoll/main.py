# #module allows us to find the working directory/file path
from datetime import date
import os

# #module will allow reading of CSV files
import csv

#create a variable (csvpath) that holds the location of the file
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')

#tell it to locate it
print(csvpath)

# #ask it what type of datatype it is
# print(type(csvpath))

vote = 0
all_votes = 0
candidates = []
printed_candidates = []
candidate_votes = {}
# prev = 0

# #open the CSV as a CSV file
with open(csvpath) as csvfile:

#  #do the same thing with the CSV reader & tell it how the info is separated
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)


# # Iterate through each row and count the number of votes
#     for row in csvreader:
#         all_votes += 1
      
#create a forloop to pull number of votes csst 
    total_votes = 0
    for row in csvreader:
            total_votes += 1
            candidate_name = row[2]
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            else:
                candidate_votes[candidate_name] = 1

# print("List of candidates who received votes:")
    for row in csvreader:
        candidate_name = row[2]
        if candidate_name not in printed_candidates:
            printed_candidates.append(candidate_name)
            unique_candidates = list(set(candidates))

max_percentage = 0
winner = ""

for candidate, vote in candidate_votes.items():
    percentage = (vote / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({vote})")
    
    if percentage > max_percentage:
        max_percentage = percentage
        winner = candidate



# # AFTER THE FOR LOOP COMPLETES}

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for candidates, vote in candidate_votes.items():
    percentage = (vote / total_votes) * 100
    print(f"{candidates}: {percentage:.3f}% ({vote})")
print("-------------------------")
print(f"The winner is: {winner}")
