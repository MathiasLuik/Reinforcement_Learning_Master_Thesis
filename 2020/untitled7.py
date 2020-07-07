# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:38:22 2020

@author: Mathias Luik
"""

import backtrader as bt
import alpaca_backtrader_api

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

store = alpaca_backtrader_api.AlpacaStore(
    key_id='PK9UJEC1G4Z0BVBQ6J77',
    secret_key='D2Ne2/8dWZ6HnZ9YyI8bD1geLVUuU5pRTe5TSpJu',
    paper=True
)

broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
cerebro.setbroker(broker)

DataFactory = store.getdata # or use alpaca_backtrader_api.AlpacaData
data0 = DataFactory(dataname='AAPL', timeframe=bt.TimeFrame.TFrame("Days"))  # Supported timeframes: "Days"/"Minutes"
cerebro.adddata(data0)

#cerebro.run(exactbars=1)
#cerebro.plot()