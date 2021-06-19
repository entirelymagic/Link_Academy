import matplotlib.pyplot as plt

p = plt.figure(facecolor="yellow")
p.suptitle("This is a subtitle", fontsize="medium")
p.add_axes([0.1, 0.3, 0.8, 0.5])
plt.plot([1, 5, 7, 2, 4, 3, 6], "o", linestyle="--", color="r")
plt.xlabel("Distanta")
plt.ylabel("Timp")
plt.show()
