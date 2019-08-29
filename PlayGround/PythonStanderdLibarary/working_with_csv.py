import csv

# in windows python add extra line while writer.writerow we need to add newline ='' paramter to ingore that.
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([4000, 2, 5])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
