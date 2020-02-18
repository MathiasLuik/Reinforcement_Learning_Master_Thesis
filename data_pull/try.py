# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:38:28 2019

@author: Mathias
"""


import requests
import json
import pandas as pd
import numpy as np
from pandas import DataFrame, Series, MultiIndex
import datetime as datetime
#from ggplot import *
#import ggplot
#%matplotlib inline
def round_time(dt=None, roundTo=60):
  
       seconds = (dt - dt.min).seconds
   
       rounding = (seconds+roundTo/2) // roundTo * roundTo
       return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
   
def get_google_finance(ticker,period = '2M'):
      
    '''Returns a data frame containing minute data for the given ticker over the given interval'''
    
    r = requests.get('http://www.google.com/finance/getprices?q='+ticker+'&i=119&p='+period+'&f=d,o,h,l,c,v')
    split = r.text.split('\n')
    df = []
    print(split)
    for word in split[7:]:
        df.append(word.split(','))
    data = DataFrame(df, columns = ['DATE','CLOSE','HIGH','LOW','OPEN','VOLUME'], dtype = 'float').dropna()
    for i in range(len(data.DATE)):
        data.DATE.ix[i] = data.DATE.ix[i].replace('a','')
    for i in range(len(data.DATE)):
        data.DATE.ix[i] = datetime.datetime.fromtimestamp(int(data.DATE.ix[i])).strftime('%Y-%m-%d %H:%M:%S')
    
    timedelta = round_time(datetime.datetime.utcnow(),60) - round_time(datetime.datetime.now(),60)
    data.DATE = pd.to_datetime(data.DATE) + timedelta
   
    
    data.index = pd.DatetimeIndex(data.DATE)
    data = data.drop('DATE', axis = 1)
    data = data[['OPEN','HIGH','LOW','CLOSE','VOLUME']]
    return data
print(get_google_finance('AAPL'))