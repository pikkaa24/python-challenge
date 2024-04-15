#Modules
import os 
import csv
from collections import Counter

#Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

#Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #read header row
    csv_header = next(csvreader)

    #set tracking variables to zero
    total_votes = 0
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
    candidates = []
    
    for row in csvreader:

        #add to total vote
        total_votes += 1

        #add candidate name to list
        candidates.append(row[2])

    #clean duplicates from candidate list
    clean_candidates = []
    candidate_count = Counter(candidates)
    vote_count = []
    
    #count iterations of names and add number of votes and name to list 
    for item, count in candidate_count.items():
        vote_count.append(count)
        clean_candidates.append(item)

#print results to terminal
print("Election Results") 
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------")  

#set variable to hold most votes
most_votes = 0

#set variable to hold winner name
winner = ""

#print candidate name, percentage of votes, and number of votes from lists
for x in clean_candidates:
    index = clean_candidates.index(x)
    votes = int(vote_count[index])
    percent = round(((votes) / total_votes) * 100, 3)
    print(f"{clean_candidates[index]}: {percent}% ({vote_count[index]})")

    #find name with most votes and set as winner
    if votes > most_votes:
        most_votes = votes
        winner = clean_candidates[index]
print("------------------------------") 
print(f"Winner: {winner}")
print("------------------------------")     

#print results to .txt
with open("output.txt", "a") as f:
    print("Election Results", file=f) 
    print("------------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("------------------------------", file=f)
    for x in clean_candidates:
        index = clean_candidates.index(x)
        votes = int(vote_count[index])
        percent = round(((votes) / total_votes) * 100, 3)
        print(f"{clean_candidates[index]}: {percent}% ({vote_count[index]})", file=f)
    print("------------------------------", file=f) 
    print(f"Winner: {winner}", file=f)
    print("------------------------------", file=f) 