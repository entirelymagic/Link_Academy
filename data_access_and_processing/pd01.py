dt1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
dt2 = pd.Series([2, 3, 4])

dt: DataFrame = pd.DataFrame([dt1, dt2])
dt.plot()
plt.show()
