# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
months = 0
net_total = 0
net_change_list = []

# Add more variables to track other necessary financial data
greatest_profits_increase = ["",0]
greatest_profits_decrease = ["",100000000000000]
month_of_change = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    months = months +1

    # Track the total and net change
    net_total = net_total + int(first_row[1])
    prev_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        months = months + 1
        net_total = net_total + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_profits_increase[1]:
            greatest_profits_increase[0] = row[0]
            greatest_profits_increase[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_profits_decrease[1]:
            greatest_profits_decrease[0] = row[0]
            greatest_profits_decrease[1] = net_change


# Calculate the average net change across the months
monthly_change = sum(net_change_list) / len(net_change_list)


# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${net_total}\n"
    f"Average  Change: ${monthly_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_profits_increase[0]} (${greatest_profits_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_profits_decrease[0]} (${greatest_profits_decrease[1]})\n")

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


with open(file_to_output, "w") as txt_file:
    txt_file.write(output)