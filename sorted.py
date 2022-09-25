import csv

data = []

with open("archive_dataset.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for data_point in  planet_data:
    data_point[2] = data_point[2].lower()

with open("archive_dataset_sorted.csv", "a+") as f:
    terow(headers)
    csvwriter.writerows(planet_csvwriter = csv.writer(f)
    csvwriter.wridata)

with open('archive_dataset_sorted.csv') as input, open('archive_dataset_sorted1.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)



