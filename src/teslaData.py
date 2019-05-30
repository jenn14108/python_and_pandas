import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../tsla_price-history-05-30-2019.csv")
#get rid of pandas indexing of data
data.set_index("Time", inplace = True)
print(data.head()) #prints first 5 rows of data
