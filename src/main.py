import csv
import argparse

from Entry import Entry
from generators import Minimal, Temporal

def read_csv_file(path):

    result = []

    with open(path, "r") as input_file:
        reader = csv.reader(input_file)
        result = [Entry(row) for row in reader]

    return result

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description = "This is a simple converter from idol branch-and-bound tree csv files to dot.\nRefer to https://github.com/hlefebvr/idol.")
    
    parser.add_argument("--path", required=True, help="Path to the csv file")
    parser.add_argument("--output", help="Output filename")
    parser.add_argument("--theme", choices=["minimal", "degradation", "centered-degradation", "temporal", "infeasibility", "debug"], help="Optional theme argument")
    
    args = parser.parse_args()

    data = read_csv_file(args.path)

    builder = None
    if args.theme == "temporal": builder = Temporal(data)
    else: builder = Minimal(data)

    output = "branch_and_bound.dot" if args.output is None else args.output

    builder.build(output)

if __name__ == "__main__":
    main()
