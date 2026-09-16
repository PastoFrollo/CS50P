import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
if len(sys.argv) > 3:
    print("Too much command-line arguments")
    sys.exit()
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    print("Not CSV files")
    sys.exit()

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        data = []
        for student in reader:
            [surname, name] = student["name"].split(', ')
            data.append({"first": name, "last": surname, "house": student["house"]})

except FileNotFoundError:
    print("File not found")
    sys.exit()

with open(sys.argv[2], "w",  newline = "") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

    writer.writeheader()
    writer.writerows(data)