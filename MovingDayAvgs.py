# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
from yahoo_finance import Share

yahoo = Share('YHOO')
print (yahoo.get_200day_moving_avg())
