# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:16:19 2016

@author: Cordell
"""

class Account:
    def __init__(self,initAmount,stockSymb):
        self.startAmount = initAmount
        self.stock = stockSymb
        
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