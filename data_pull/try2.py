# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:08:47 2019

@author: Mathias
"""

#import iex_data as IEX
#iex = IEX.API()
#iex.get_latest_trade(['AAPL', 'MSFT'])
from datetime import datetime  
from datetime import timedelta  
from iexfinance.stocks import Stock
from iexfinance.altdata import get_social_sentiment
from datetime import datetime
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import get_historical_intraday
import pandas as pd

df = pd.DataFrame()

#n_days=30
n_days=4
stock_name="AAPL"
#df.append(data)
#date = datetime(2018, 11, 27)
#starttime=datetime(2019, 3, 20)
endtime=datetime(2019, 3, 23)
#starttime=endtime-timedelta(days=30)
#starttime=endtime-timedelta(days=4)
for day in range(n_days):
    which_date=endtime - timedelta(days=n_days) + timedelta(days=day)
    #which_date=datetime(2019, 2, 22)
    daily_data=get_historical_intraday(stock_name, which_date, output_format='pandas')
    #print(daily_data)
    if not daily_data.empty:
        
        df=df.append(daily_data)
        #print(df)
    #if daily_dataprint(daily_data)
print(df)
#print(df.columns.values)
#['average' 'changeOverTime' 'close' 'date' 'high' 'label' 'low'
 #'marketAverage' 'marketChangeOverTime' 'marketClose' 'marketHigh'
# 'marketLow' 'marketNotional' 'marketNumberOfTrades' 'marketOpen'
 #'marketVolume' 'notional' 'numberOfTrades' 'open' 'volume']
#daily_data1=get_historical_intraday("AAPL", datetime(2019, 2, 21), output_format='pandas')
#daily_data2=get_historical_intraday("AAPL", datetime(2019, 2, 22), output_format='pandas')
#print(daily_data2)
#s=daily_data1.append(daily_data2)
#
#new=df.append(daily_data1)
#new=new.append(daily_data2)
#s3=pd.concat(df,daily_data1)
#s3=pd.concat([new,daily_data2])
#print(new)
#df.append(daily_data1)
#print(daily_data1.columns())
#which_date=datetime(2019, 2, 22)
#daily=get_historical_intraday("AAPL", datetime(2019, 2, 22), output_format='pandas')  
#if daily.empty:
  #  print("aa")  
#print(df)

#dataframe=pd


#print(df)

#df=get_historical_intraday("AAPL", output_format='pandas')
#print(df)
#print(a)
#df.plot()
#df.plt.show()