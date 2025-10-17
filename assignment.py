import csv


with open("student_data.csv") as data:
    data_reader = csv.reader(data)
    header = next(data_reader)
    rows = list(data_reader)

header.append("Grade")
for row in rows:
    per = float(row[5])
    if per > 80:
        grade ="A+"
    elif per > 70 and per < 80:
        grade ="B"
    elif per > 60 and per < 70:
        grade ="C"
    elif per > 50 and per < 60:
        grade ="D"
    else:
        grade ="Fail"
    row.append(grade)

with open("student_data_with_grades.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

from pprint import pprint
pprint(rows)



