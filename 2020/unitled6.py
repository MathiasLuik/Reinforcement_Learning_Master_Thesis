# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:25:28 2020

@author: Mathias Luik
"""


import backtrader as bt
import alpaca_backtrader_api
import pandas as pd

ALPACA_API_KEY_ID = 'PK9UJEC1G4Z0BVBQ6J77'
ALPACA_SECRET_KEY ='D2Ne2/8dWZ6HnZ9YyI8bD1geLVUuU5pRTe5TSpJu'

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

is_live = False

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

store = alpaca_backtrader_api.AlpacaStore(ALPACA_API_KEY_ID,ALPACA_SECRET_KEY)

if is_live:
    broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
    cerebro.setbroker(broker)
else:
    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.0)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=20)

DataFactory = store.getdata # or use alpaca_backtrader_api.AlpacaData
if is_live:
    data0 = DataFactory(
        dataname='AAPL',
        timeframe=bt.TimeFrame.TFrame("Minutes"),
        )
else:
    
    data0 = DataFactory(
            dataname='AAPL',
            timeframe=bt.TimeFrame.TFrame("Minutes"),
            fromdate=pd.Timestamp('2018-11-15'),
            todate=pd.Timestamp('2018-11-17'),
            historical=True)
cerebro.adddata(data0)

cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()