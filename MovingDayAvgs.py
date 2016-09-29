# -*- coding: utf-8 -*-
"""
Driver Function

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
from yahoo_finance import Share
import math
from Decisions import *
from Checks import *
from ScreenOutput import *
    
def main():
    decisions = Decisions() #Creates empty instance of Decisions class
    checks = Checks() #Creates empty instance of Checks Class
    display = ScreenOutput()
    currentAmountToTrade = 1000 #$1000 US Dollars   will become a system arg
    yahoo = Share('YHOO') #Creates yahoo instance of Share type object
    currPrice = yahoo.get_price() 
    fiftyDayMovingPrice = yahoo.get_50day_moving_avg()
    twoHundredMovingPrice = yahoo.get_200day_moving_avg()
    display.displayGreetings()
    
if __name__ == "__main__":
    main()