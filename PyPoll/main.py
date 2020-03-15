# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Read ElectionData dataset
csvpath = os.path.join('Resources', 'election_data.csv')

# Total number of votes cast
total_votes = 0

# A complete list of candidates who received votes
election = {}
candidates = []
winner = "NoOne"
winner_total = 0

with open(csvpath) as csvfile:
	
	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first (skip this step if there is now header)
	csv_header = next(csvreader)

	for row in csvreader:

		total_votes += 1

		if row[2] in candidates:
			election[row[2]] += 1
		else:
			candidates.append(row[2])
			election[row[2]] = 1

print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
for candidate in election:
	#The percentage of votes each candidate won
	#The total number of votes each candidate won
	print(candidate + ": " + "{0:.3f}% (".format(election[candidate]/total_votes * 100) + str(election[candidate]) + ")")
	#The winner of the election based on popular vote.
	if election[candidate] > winner_total:
		winner = candidate
		winner_total = election[candidate]
print("---------------------")
print("Winner: " + winner)
print("---------------------")

with open("output.txt", "w") as text_file:
	print("Election Results", file=text_file)
	print("---------------------", file=text_file)
	print(f"Total Votes: {total_votes}", file=text_file)
	print("---------------------", file=text_file)
	for candidate in election:
		print(candidate + ": " + "{0:.3f}% (".format(election[candidate]/total_votes * 100) + str(election[candidate]) + ")", file=text_file)
	print("---------------------", file=text_file)
	print("Winner: " + winner, file=text_file)
	print("---------------------", file=text_file)