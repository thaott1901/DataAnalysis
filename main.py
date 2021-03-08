import pandas as pd

path = 'pydata-book-2nd/datasets/babynames/yob1880.txt'
names1880 = pd.read_csv(path, names=['name', 'sex', 'births'])
a = names1880.groupby('sex').births.sum()
print(a)
