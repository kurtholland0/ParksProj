import csv
import os

# Get the user's home directory
home_dir = os.path.expanduser("~")

# Construct the full file paths
file_path = os.path.join(home_dir, "Downloads", "Parks.csv")

def delete_zeroes(file, output):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        with open(output, "w") as output_file:
            writer = csv.writer(output_file)
            for line in reader:
                if line[6] != "0":
                    writer.writerow(line)

delete_zeroes(file_path, "ParksNoZero.csv")
