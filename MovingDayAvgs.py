# -*- coding: utf-8 -*-
"""
Driver Function

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
from yahoo_finance import Share
import argparse
from Decisions import *
from ScreenOutput import *
from Account import * 
    
def main():
    parser = argparse.ArgumentParser(description='StrategyTester.')
    parser.add_argument("symb",help="Enter Stock Symbol to Test")
    parser.add_argument("initFund",type=int,help="Enter Starting Amount to Invest With")
    args = parser.parse_args()
    account = Account(args.symb,args.initFund)
    account.createPortfolio(account.stock)

    yahoo = Share('YHOO') #Creates yahoo instance of Share type object
    currPrice = yahoo.get_price() 
    fiftyDayMovingPrice = yahoo.get_50day_moving_avg()
    twoHundredMovingPrice = yahoo.get_200day_moving_avg()
    #display.displayGreetings()
    
if __name__ == "__main__":
    main()