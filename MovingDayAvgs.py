# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
from yahoo_finance import Share
import math
from Decisions import *
from Checks import *
    
def main():
    decisions = Decisions()
    checks = Checks()
    currentAmountToTrade = 1000 #$1000 US Dollars   will become a system arg
    yahoo = Share('YHOO')
    currPrice = yahoo.get_price()
    fiftyDayMovingPrice = yahoo.get_50day_moving_avg()
    twoHundredMovingPrice = yahoo.get_200day_moving_avg()
    print("Hello User, you have $"+str(currentAmountToTrade)+ " to trade today!") #In Future, this will current amount and check if you have enough
    print("The current share price is: "+ yahoo.get_price())
    print ("The current 50 Day Moving Avg is: " +yahoo.get_50day_moving_avg()+" "+ decisions.determineAgainst50(currPrice,fiftyDayMovingPrice))
    print ("The current 200 Day Moving Avg is: " + yahoo.get_200day_moving_avg() +" "+ decisions.determineAgainst200(currPrice,twoHundredMovingPrice))
    print ("You can purchase "+ str(checks.checkHowMany(currentAmountToTrade,currPrice)) + " shares of "+yahoo.symbol)
    print (42.8042*23)

if __name__ == "__main__":
    main()