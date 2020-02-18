# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:18:40 2019

@author: Mathias
"""

import pickle

example_dict = {1:"6",2:"2",3:"f"}

pickle_in = open("dmass.pickle","rb")
example_dict = pickle.load(pickle_in)
pickle_in.close()