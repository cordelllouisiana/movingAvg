# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:16:19 2016

@author: Cordell
"""
import math
from Decisions import *
from ScreenOutput import *

class Account:
    decisions = Decisions() #Creates empty instance of Decisions class
    display = ScreenOutput()
    def __init__(self,stockSymb,initAmount):
        self.startAmount = initAmount
        self.stock = stockSymb
        self.currentAmountToTrade = initAmount        
    
    def createPortfolio(self,stock):
        return "Go Pee"
        
        
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