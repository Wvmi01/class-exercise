import argparse
import csv
import sys
from pathlib import Path
import logging

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
# Set up logging (before parser)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S")

# Create a module-level logger
logger = logging.getLogger(__name__)

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

if args.verbose:
    logger.setLevel(logging.DEBUG)

logger.debug(f"Arguments parsed: filename={args.input}")

#Check if the file exists
#p = Path(args.input)
#if not p.is_file():
#    print(f"File not found: '{args.input}'")
#    sys.exit(1)

#print(f"File validated: '{args.input}'")

p = Path(args.input)
if not p.is_file():
    logger.error(f"File not found: '{args.input}'")
    sys.exit(1)

logger.info(f"File validated: '{args.input}'")

# Sep 6: check the data:
logger.debug(f"Loading data from: {args.input}")

header, data, missing_rows = check_data(args.input)

logger.info(f"Loaded {len(data)} rows")

# After adding info:
if len(data) == 0:
    logger.error("Input file contains no data; cannot continue")
    sys.exit(1)

# Step 8: Rows w/ missing values
for row_number in missing_rows:
    logger.warning(f"Row {row_number} has missing values")

# Save the report:
with open(args.output, "w") as f:
    f.write(f"Number of rows: {len(data)}\n")
    f.write(f"Number of columns: {len(header)}\n")
    f.write(f"Number of rows with missing values: {len(missing_rows)}\n")

logger.info(f"Report saved to {args.output}")