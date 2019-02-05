#import packages
import pandas as pd
import numpy as np
import sklearn
#to plot within notebook
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
#%matplotlib inline
#matplotlib.use("Agg")

#setting figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10

#for normalizing data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

#read the file
df = pd.read_csv('data/GSPC.csv')

#print the head
#plot
plt.figure(figsize=(16,8))
plt.plot(df['Close'], label='Close Price history')
#creating dataframe with date and the target variabl
df.head()
#setting index as date
df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']

data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0,len(df)),columns=['Date', 'Close'])

for i in range(0,len(data)):
     new_data['Date'][i] = data['Date'][i]
     new_data['Close'][i] = data['Close'][i]
#splitting into train and validation
train = new_data[:987]
valid = new_data[987:]

train['Date'].min(), train['Date'].max(), valid['Date'].min(), valid['Date'].max()

