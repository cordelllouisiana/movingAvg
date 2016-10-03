# -*- coding: utf-8 -*-
"""
Driver Function

This is a script that searches the market and checks which
stock are currently priced above their 200 day moving avg.
"""
import argparse
from Account import * 
from ScreenOutput import *
from stockClient import *
    
def main():
    greet = ScreenOutput()
    parser = argparse.ArgumentParser(description='StrategyTester.')
    parser.add_argument("symb",help="Enter Stock Symbol to Test")
    parser.add_argument("initFund",type=int,help="Enter Starting Amount to Invest With")
    args = parser.parse_args()
    account = Account(args.symb,args.initFund)
    sym= args.symb
    curr = account.currentAmountToTrade
    greet.displayGreetings(curr,sym)
    #Get How Many User Can Buy
    
    account.createPortfolio(account.stock)
    client = stockClient()
    print(client.get_price())

    
if __name__ == "__main__":
    main()
    
    