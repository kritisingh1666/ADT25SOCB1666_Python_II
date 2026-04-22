import json
import csv

# Read JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)   # Load JSON array

# Get headers (keys from first object)
headers = data[0].keys()

# Write to CSV file
with open("output.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    
    writer.writeheader()   # Write column names
    writer.writerows(data) # Write data rows

print("JSON data has been converted to CSV successfully.")
