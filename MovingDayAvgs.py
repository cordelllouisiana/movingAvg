# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
from yahoo_finance import Share

def determineAgainst50(curr,fifty):
    if(curr > fifty):
        decision = "buy"
    elif(fifty >= curr):
        decision = "sell"
        
    return decision
    
def main():
    yahoo = Share('YHOO')
    currPrice = yahoo.get_price()
    fiftyDayMovingPrice = yahoo.get_50day_moving_avg()
    twoHundredMovingPrice = yahoo.get_200day_moving_avg()
    print("The current share price is: "+ yahoo.get_price())
    print ("The current 50 Day Moving Avg is: " +yahoo.get_50day_moving_avg()+" "+ determineAgainst50(currPrice,fiftyDayMovingPrice))
    print ("The current 200 Day Moving Avg is: " + yahoo.get_200day_moving_avg())

if __name__ == "__main__":
    main()