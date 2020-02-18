# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:08:15 2019

@author: Mathias
"""
#from quantopian.research import prices, symbols
#from zipline.api import symbol, symbols
#from zipline.api import attach_pipeline, pipeline_output #from quantopian.algorithm import attach_pipeline, pipeline_output  
#from quantopian.pipeline import Pipeline  
from zipline.api import schedule_function,date_rules,time_rules,record,order_target_percent
import zipline.api
#from quantopian.pipeline.data.builtin import USEquityPricing  
#from quantopian.pipeline.factors import AverageDollarVolume  
import pandas as pd 
# Use the previous 10 bars' movements to predict the next movement.

# Use a random forest classifier. More here: http://scikit-learn.org/stable/user_guide.html
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def initialize(context):
    context.security = sid(8554) # Trade SPY
    context.model = RandomForestRegressor()

    context.lookback = 3 # Look back 3 days
    context.history_range = 400 # Only consider the past 400 days' history

    # Generate a new model every week
    schedule_function(create_model, date_rules.week_end(), time_rules.market_close(minutes=10))

    # Trade at the start of every day
    schedule_function(trade, date_rules.every_day(), time_rules.market_open(minutes=1))

def create_model(context, data):
    # Get the relevant daily prices
    recent_prices = data.history(context.security, 'price', context.history_range, '1d').values
    
    # Get the price changes
    price_changes = np.diff(recent_prices).tolist()

    X = [] # Independent, or input variables
    Y = [] # Dependent, or output variable
    
    # For each day in our history
    for i in range(context.history_range-context.lookback-1):
        X.append(price_changes[i:i+context.lookback]) # Store prior price changes
        Y.append(price_changes[i+context.lookback]) # Store the day's price change

    context.model.fit(X, Y) # Generate our model

def trade(context, data):
    if context.model: # Check if our model is generated
        
        # Get recent prices
        recent_prices = data.history(context.security, 'price', context.lookback+1, '1d').values
        
        # Get the price changes
        price_changes = np.diff(recent_prices).tolist()
        
        # Predict using our model and the recent prices
        prediction = context.model.predict(price_changes)
        record(prediction = prediction)
        
        # Go long if we predict the price will rise, short otherwise
        if prediction > 0:
            order_target_percent(context.security, 1.0)
        else:
            order_target_percent(context.security, -1.0)