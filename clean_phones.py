import csv

with open('brudne_dane.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

for row in rows[1:]:
    cleaned_phone = (
        row[1]
        .strip()
        .replace(" ", "")
        .replace("-", "")
    )
    row[1] = cleaned_phone

with open('czyste_dane.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Gotowe! Sprawdź plik 'czyste_dane.csv'")