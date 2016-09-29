# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:51:09 2016

@author: Cordell
"""

class Checks:
    def checkHowMany(self,curBankAmount,currPrice):
    #Use Constant for trading
        tradingFee = 10 #$10 US Dollars
        curBankAmount = float(curBankAmount)
        currPrice = float(currPrice)
        howMany = ((curBankAmount - tradingFee)/(currPrice))
        howMany = int(howMany)
        return howMany
    
    def checkWhenSell():  #need to write a function to see when should I sell 
        return null