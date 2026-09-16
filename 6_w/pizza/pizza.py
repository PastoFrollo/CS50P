import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
if len(sys.argv) < 2:
    print("Too much command-line arguments")
    sys.exit()
if not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit()

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers = "keys", tablefmt = "grid"))

except FileNotFoundError:
    print("File not found")
    sys.exit()