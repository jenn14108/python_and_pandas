import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../tsla_price-history-05-30-2019.csv")
#used to figure out the index in which to delete the last row of data
#print(data.tail())
data = data.drop([102])

#get rid of pandas indexing of data
data.set_index("Time", inplace = True)
#print(data.head()) #prints first 5 rows of data
data = data.iloc[::-1] #reverse the dataset, I want January - May
#print(data.head())

#create a new graph, set title and axis labels
teslaStockPrice = data.plot(y="Last",title="Tesla 2019 Historical Stock Price")
teslaStockPrice.set_xlabel("Date")
teslaStockPrice.set_ylabel("Stock Price")
plt.show()
