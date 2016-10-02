# -*- coding: utf-8 -*-
"""
Driver Function

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
import argparse
from Account import * 
from ScreenOutput import *
    
def main():
    parser = argparse.ArgumentParser(description='StrategyTester.')
    parser.add_argument("symb",help="Enter Stock Symbol to Test")
    parser.add_argument("initFund",type=int,help="Enter Starting Amount to Invest With")
    args = parser.parse_args()
    account = Account(args.symb,args.initFund)
    curr = account.currentAmountToTrade
    greet = ScreenOutput()
    greet.displayGreetings(curr)
    account.createPortfolio(account.stock)

    #display.displayGreetings()
    
if __name__ == "__main__":
    main()
    
    