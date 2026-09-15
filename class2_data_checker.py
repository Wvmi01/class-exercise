import argparse
import csv
import sys
from pathlib import Path

def check_data(filename):
    """Read the CSV file and check for missing values."""
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]
    missing_rows = []

    for row_number, row in enumerate(data, start=2):
        if any(value == "" for value in row):
            missing_rows.append(row_number)

    return header, data, missing_rows

# TO-DO: 
# Create an ArgumentParser:
parser = argparse.ArgumentParser(description="Analyze a data file")
# Add a named argument (required):
parser.add_argument("--input",
                    "-i",
                    required=True,
                    help="Path to input CSV file")
# Add a named argument (optional):
parser.add_argument("--output",
                    "-o",
                    default="results.txt",
                    help="Output file path")
# Add a boolean flag
parser.add_argument("--verbose",
                    "-v",
                    action="store_true",
                    help="Show detailed DEBUG messages")
# Parse the command-line arguments
args = parser.parse_args()

#Check if the file exists
p = Path(args.input)
if not p.is_file():
    print(f"File not found: '{args.input}'")
    sys.exit(1)

print(f"File validated: '{args.input}'")

# Check the data:
header, data, missing_rows = check_data(args.input)

# Save the report:
with open(args.output, "w") as f:
    f.write(f"Number of rows: {len(data)}\n")
    f.write(f"Number of columns: {len(header)}\n")
    f.write(f"Number of rows with missing values: {len(missing_rows)}\n")