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
    key_id='PK0JQXH59LXYYEUB6J91',
    secret_key='Wg8H5lozfpE9JzZJw/BjuESek4psKZ34DwKdW4Io',
    paper=True
)

broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
cerebro.setbroker(broker)

DataFactory = store.getdata # or use alpaca_backtrader_api.AlpacaData
data0 = DataFactory(dataname='AAPL', timeframe=bt.TimeFrame.TFrame("Days"))  # Supported timeframes: "Days"/"Minutes"
cerebro.adddata(data0)

cerebro.run(exactbars=1)
cerebro.plot()


"""
import alpaca_trade_api as tradeapi

api = tradeapi.REST('PK0JQXH59LXYYEUB6J91', 'Wg8H5lozfpE9JzZJw/BjuESek4psKZ34DwKdW4Io')
account = api.get_account()
api.list_positions()
print(api.list_positions())

import alpaca_trade_api as tradeapi

api = tradeapi.REST()

# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('AAPL', 'day', limit=5)
aapl_bars = barset['AAPL']

# See how much AAPL moved in that timeframe.
week_open = aapl_bars[0].o
week_close = aapl_bars[-1].c
percent_change = (week_close - week_open) / week_open
print('AAPL moved {}% over the last 5 days'.format(percent_change))

api = tradeapi.REST('<key_id>', '<PKCH1RAY4DZ0A3T91H92>')#'<secret_key>'
# Daily OHLCV dataframe
aapl_daily = api.polygon.historic_agg('day', 'AAPL', limit=1000).df
# Dictionary of most recent earning stats for each company
list_earning = api.polygon.earnings(['MSFT','FB','AMZN'])
# Returns a list articles and their meta-data
tsla_news = api.polygon.news('TSLA')

"""

"""
api = tradeapi.REST('PK0JQXH59LXYYEUB6J91', 'Wg8H5lozfpE9JzZJw/BjuESek4psKZ34DwKdW4Io')
# Lists currently open trades
positions = api.list_positions()
# Places a limit order
api.submit_order('AAPL',10,'buy','limit','gtc',170.50)

# Lists all open orders
orders = api.list_orders()
print(orders)
"""

#import alpaca_trade_api as tradeapi
"""
import os
import argparse
import pandas as pd
import alpaca_trade_api as ata
import datetime as dt
from pytz import timezone

os.environ['APCA_API_KEY_ID']='PK0JQXH59LXYYEUB6J91'
os.environ['APCA_API_SECRET_KEY']='Wg8H5lozfpE9JzZJw/BjuESek4psKZ34DwKdW4Io'

def main(symbol,date,start,ticks,cond):
    full_date = date+" "+start
    st = dt.datetime.strptime(full_date, '%Y-%m-%d %H:%M:%S')
    st = timezone('US/Eastern').localize(st)
    st = int(st.timestamp())*1000
    trades = ata.REST().polygon.historic_trades(symbol, date, offset=st, limit=ticks)
    trades.df.reset_index(level=0, inplace=True)
    #convert exchange numeric codes to names for readability
    exchanges = ata.REST().polygon.exchanges()
    ex_lst = [[e.id,e.name,e.type] for e in exchanges]
    dfe = pd.DataFrame(ex_lst,columns=['exchange','exch','excode'])
    trades.df['exchange'] = trades.df['exchange'].astype(int)
    df = pd.merge(trades.df,dfe,how='left',on='exchange')
    df = df[df.exchange!=0]
    df.drop('exchange', axis=1, inplace=True)
    if cond:
        #convert sale condition numeric codes to names for readability
        conditions = ata.REST().polygon.condition_map()
        c = conditions.__dict__['_raw']
        c = {int(k):v for k,v in c.items()}
        df['condition1'] = df['condition1'].map(c)
        df['condition2'] = df['condition2'].map(c)
        df['condition3'] = df['condition3'].map(c)
        df['condition4'] = df['condition4'].map(c)
    else:
        df.drop(['condition1','condition2','condition3','condition4'], axis=1, inplace=True)
    print(df.to_string())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', type=str, default='SPY', help='symbol you want to get data for')
    parser.add_argument('--date', type=str, default='2018-09-19', help='date you want to get data for')
    parser.add_argument('--start', type=str, default='09:30:00', help='start time you want to get data for')
    parser.add_argument('--ticks', type=int, default=10000, help='number of ticks to retrieve')
    parser.add_argument('--conditions', action='store_true', default=False)
    args = parser.parse_args()
    main(args.symbol,args.date,args.start,args.ticks,args.conditions)
"""    