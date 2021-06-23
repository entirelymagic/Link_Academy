import pandas as pd
import matplotlib.pyplot as plt

dt2 = pd.DataFrame([["Razvan", 18], ["Andrei", 22], ["Elvis", 33]], columns=["Student", "Age"])

dt2.plot.bar(x="Student", y="Age")
plt.show()

dt = pd.DataFrame([
    ["Italy", "Milan", 7],
    ["Spain", "Real", 13],
    ["Germany", "Bayern", 6],
    ["Spain", "Barcelona", 5]
],
    columns=["Country", "Team", "Trophies"]
)
dt.plot.scatter(x="Team", y="Trophies")
plt.show()
