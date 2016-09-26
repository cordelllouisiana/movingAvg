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
def determineAgainst200(curr,twoHundred):
    if(curr > twoHundred):
        decision = "buy"
    elif(twoHundred >= curr):
        decision = "sell"
        
    return decision
    
    
    
def main():
    currentAmountToTrade = 1000 #$1000 US Dollars
    yahoo = Share('YHOO')
    currPrice = yahoo.get_price()
    fiftyDayMovingPrice = yahoo.get_50day_moving_avg()
    twoHundredMovingPrice = yahoo.get_200day_moving_avg()
    print("Hello User, you have $"+str(currentAmountToTrade)+ " to trade today!") #In Future, this will current amount and check if you have enough
    print("The current share price is: "+ yahoo.get_price())
    print ("The current 50 Day Moving Avg is: " +yahoo.get_50day_moving_avg()+" "+ determineAgainst50(currPrice,fiftyDayMovingPrice))
    print ("The current 200 Day Moving Avg is: " + yahoo.get_200day_moving_avg() +" "+ determineAgainst200(currPrice,twoHundredMovingPrice))

if __name__ == "__main__":
    main()