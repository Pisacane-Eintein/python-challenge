
import os
import csv

election_csv = os.path.join("..","PyPoll", "election_data.csv")

votes = []
stockham = []
degette = []
doane = []


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        votes.append(row[2])
        if row[2] == "Charles Casper Stockham":
            stockham.append(row[2]) 
        elif (row[2] == "Diana DeGette"):
            degette.append(row[2])
        else:
            doane.append(row[2])
    total_votes = len(votes)
    
    votes_stockham = len(stockham)
    stockham_total = round(((votes_stockham/total_votes) * 100),3)

    votes_degette = len(degette)
    degette_total = round(((votes_degette/total_votes) * 100),3)
    
    votes_doane = len(doane)
    doane_total = round(((votes_doane/total_votes) * 100),3)

    winner = max(votes_stockham, votes_degette, votes_doane )
    if winner == votes_stockham:
        winner_name = "Charles Casper Stockham"
    elif winner == votes_degette:
        winner_name = "Diana DeGette"
    else:
        winner_name = "Raymon Anthony Doane"

 # Add summary table intro headers to column 0
    for row in range(0,1):
        
        print('')
        print('Election Results') 
        print('')
        print('---------------------------')
        print('')
        print(f'Total Votes:  {total_votes}')
        print('')
        print('---------------------------')
        print('')
        print(f'Charles Casper Stockham: {stockham_total}% ({votes_stockham})  ')
        print('')
        print(f'Diana DeGette: {degette_total}% ({votes_degette})  ')
        print('')
        print(f'Raymon Anthony Doane: {doane_total}% ({votes_doane})  ')
        print('')
        print('---------------------------')
        print('')
        print(f'Winner: {winner_name}  ')
        print('')
        print('---------------------------')

# write to a new csv file
import csv

# write to a new csv file
with open('Analysis/election_results.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    

    # Add summary table intro headers to column 0
    for row in range(0,1):
        
        writer.writerow(['Election Results']) 
        writer.writerow(['---------------------------'])
        writer.writerow([f'Total Votes:  {total_votes}'])
        writer.writerow(['---------------------------'])
        writer.writerow([f'Charles Casper Stockham: {stockham_total}% ({votes_stockham})  '])
        writer.writerow([f'Diana DeGette: {degette_total}% ({votes_degette})  '])
        writer.writerow([f'Raymon Anthony Doane: {doane_total}% ({votes_doane})  '])
        writer.writerow(['---------------------------'])
        writer.writerow([f'Winner: {winner_name}  '])
        writer.writerow(['---------------------------'])

  
    