import matplotlib.pyplot as plt
import csv

countries = {}
with open("countries.csv", "r") as f:
    for row in csv.reader(f):
        countries[row[1]] = int(row[2])

labels = countries.keys()
sizes = countries.values()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
