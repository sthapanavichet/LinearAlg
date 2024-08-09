import pandas as pd
dataset = pd.read_csv(r'C:\Users\sthap\OneDrive\Desktop\Projects\Linear Algeba\lab 4\pizza.csv')
print(dataset.head())
dataset.corr()

A = np.array([1,3], [1,3])
