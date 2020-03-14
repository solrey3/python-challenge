# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Read BudgetData dataset
csvpath = os.path.join('Resources', 'budget_data.csv')

month_count = 0
net_total = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(csvpath) as csvfile:

	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	#print(csvreader)

	# Read the header row first (skip this step if there is now header)
	csv_header = next(csvreader)

	# Read each row of data after the header
	for row in csvreader:
		#print(row)

		#print(month_count)

		# The total number of months included in the dataset
		month_count = month_count + 1

		# The net total amount of "Profit/Losses" over the entire period
		net_total = net_total + float(row[1])

		# The greatest increase in profits (date and amount) over the entire period
		if float(row[1]) > greatest_increase:
			greatest_increase = float(row[1])
			greatest_increase_month = row[0]

		# The greatest decrease in losses (date and amount) over the entire period
		if float(row[1]) < greatest_decrease:
			greatest_decrease = float(row[1])
			greatest_decrease_month = row[0]

	# The average of the changes in "Profit/Losses" over the entire period
	average = net_total / month_count

	print("Financial Analysis")
	print("-----------------------------------------------------")
	print(f"Total Months: {month_count}")
	print("Total: $" + "{0:.2f}".format(net_total))
	print("Average: $" + "{0:.2f}".format(average))
	print("Greatest Increase in Profits: " + greatest_increase_month + " (${0:.2f})".format(greatest_increase))
	print("Greatest Decrease in Profits: " + greatest_decrease_month + " (${0:.2f})".format(greatest_decrease))
	


