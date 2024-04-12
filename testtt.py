table = []

with open('tabletwo', "r") as file:
    for line in file:
        line = line.split("\n")[0]
        line = line.split("\t")
        rows = []
        for num in line: 
            rows.append(num)

        table.append(rows)

for row in table:
    print(row, end= ",\n")