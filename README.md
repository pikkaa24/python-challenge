# python-challenge

PyBank financial analysis tracks changes for given data and output total number of months, total profit/loss, average change between months, and greatest profit and loss between months. 

PyBank tallies votes during an election. It outputs the total number of votes cast, and the number and percent of votes for each candidate, then the winner of the election.

Referenced https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file to export .txt file with terminal printout

Reference https://note.nkmk.me/en/python-os-getcwd-chdir/ to set directory to print txt file into

Adapted following code from Xpert Leaning Assistant to count votes:
    from collections import Counter

    # Sample list with items
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'apple']

    # Use Counter to count the occurrences of each item in the list
    item_counts = Counter(my_list)

    # Print the count of iterations for each item
    for item, count in item_counts.items():
        print(f"{item}: {count} iterations")   
