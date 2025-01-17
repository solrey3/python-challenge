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
change_total = 0
change_total_sum = 0
previous_total = 0

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
		if month_count != 0:
			change_total = float(row[1]) - previous_total
		else:
			change_total = 0

		previous_total = float(row[1])

		# The total number of months included in the dataset
		month_count = month_count + 1

		# The net total amount of "Profit/Losses" over the entire period
		net_total = net_total + float(row[1])
		change_total_sum = change_total_sum + change_total 

		# The greatest increase in profits (date and amount) over the entire period
		if change_total > greatest_increase:
			greatest_increase = change_total
			greatest_increase_month = row[0]

		# The greatest decrease in losses (date and amount) over the entire period
		if change_total < greatest_decrease:
			greatest_decrease = change_total
			greatest_decrease_month = row[0]

	# The average of the changes in "Profit/Losses" over the entire period
	average = change_total_sum / (month_count - 1)

	print("Financial Analysis")
	print("-----------------------------------------------------")
	print(f"Total Months: {month_count}")
	print("Total: $" + "{0:.2f}".format(net_total))
	print("Average: $" + "{0:.2f}".format(average))
	print("Greatest Increase in Profits: " + greatest_increase_month + " (${0:.2f})".format(greatest_increase))
	print("Greatest Decrease in Profits: " + greatest_decrease_month + " (${0:.2f})".format(greatest_decrease))

	with open("output.txt", "w") as text_file:
		print("Financial Analysis", file=text_file)
		print("-----------------------------------------------------", file=text_file)
		print(f"Total Months: {month_count}", file=text_file)
		print("Total: $" + "{0:.2f}".format(net_total), file=text_file)
		print("Average: $" + "{0:.2f}".format(average), file=text_file)
		print("Greatest Increase in Profits: " + greatest_increase_month + " (${0:.2f})".format(greatest_increase), file=text_file)
		print("Greatest Decrease in Profits: " + greatest_decrease_month + " (${0:.2f})".format(greatest_decrease), file=text_file)
	


