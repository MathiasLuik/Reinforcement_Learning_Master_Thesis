# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:48:47 2020

@author: Mathias Luik
"""

import alpaca_backtrader_api
import backtrader as bt
from datetime import datetime
ALPACA_API_KEY = 'PKV5297J2WUES7E6RZN5' #paper
ALPACA_SECRET_KEY ='6ne0oEGvokPNBB3KvY/TfosIaXPK6KHDoXpSr8KA' #paper
#ALPACA_API_KEY = 'AKF1NX5QKZIZWQEXE9JP' #real
#ALPACA_SECRET_KEY ='zzIr8PbfRFZpxZHIQrepcAF1v1BEhM8QJzSuDZdd' #real

ALPACA_PAPER = True


class SmaCross(bt.SignalStrategy):
  def __init__(self):
    sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
    crossover = bt.ind.CrossOver(sma1, sma2)
    self.signal_add(bt.SIGNAL_LONG, crossover)


cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

store = alpaca_backtrader_api.AlpacaStore(
    #key_id=ALPACA_API_KEY,
    #secret_key=ALPACA_SECRET_KEY,
    #paper=ALPACA_PAPER
    #, base_url='https://data.alpaca.markets/v1'
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    paper=ALPACA_PAPER
)

if not ALPACA_PAPER:
  broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
  cerebro.setbroker(broker)

DataFactory = store.getdata  # or use alpaca_backtrader_api.AlpacaData
data0 = DataFactory(dataname='AAPL', historical=True, fromdate=datetime(
    2019, 1, 1), timeframe=bt.TimeFrame.Days)
print(data0)
cerebro.adddata(data0)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()