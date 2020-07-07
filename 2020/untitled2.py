# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:58:18 2020

@author: Mathias Luik
"""

import alpaca_backtrader_api
import backtrader as bt
from datetime import datetime
import pytz

ALPACA_API_KEY = 'PKV5297J2WUES7E6RZN5' #paper
ALPACA_SECRET_KEY ='6ne0oEGvokPNBB3KvY/TfosIaXPK6KHDoXpSr8KA' #paper
ALPACA_PAPER = False


class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

store = alpaca_backtrader_api.AlpacaStore(
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    paper=ALPACA_PAPER
)

if not ALPACA_PAPER:
    broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
    cerebro.setbroker(broker)
timezone = pytz.timezone("America/Los_Angeles")
DataFactory = store.getdata  # or use alpaca_backtrader_api.AlpacaData
data0 = DataFactory(dataname='AAPL', historical=True, fromdate=datetime(
    2020, 2, 1), timeframe=bt.TimeFrame.Days, tz=timezone)
cerebro.adddata(data0)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
#print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
##cerebro.plot()