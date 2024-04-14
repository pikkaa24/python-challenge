#Modules
import os 
import csv

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

        candidates.append(row[2])

        #add vote to candidate
        #if row[2] == "Charles Casper Stockham":
            #stockham_votes += 1

        #elif row[2] == "Diana DeGette":
            #degette_votes += 1

        #elif row[2] == "Raymon Anthony Doane":
            #doane_votes += 1

    #clean duplicates from candidate list
    candidates = list(set(candidates))
    vote_count = []
    
    #fill in 0 in vote count list for each candidate in list
    for x in candidates:
        #print(candidates.index(x))
        #index = candidates.index[x]
        vote_count.append(0)

    for row in csvreader:
        for x in candidates:
            print(candidates(x))
            #if row[2] == candidates(x):
                #vote_count[x] += 1
    
    #print(vote_count)

    
    #for row in csvreader:
     #   for x in range(len(candidates)):
      #      if row[2] == candidates[x]:
       #         vote_count[x] += 1
    #print(vote_count)
        


