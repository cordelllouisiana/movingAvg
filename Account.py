# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:16:19 2016

@author: Cordell
"""
import math
from Decisions import *
from ScreenOutput import *
from yahoo_finance import Share

class Account:
    decisions = Decisions() #Creates empty instance of Decisions class
    display = ScreenOutput()
    portfolio = []
    holdings = {}
   # accountBalance = 0.0;
    currentAmountToTrade = 0.0

    
    def __init__(self,stockSymb,initAmount):
        self.startAmount = initAmount
        self.stock = Share(stockSymb)
        self.currentAmountToTrade = initAmount
        
    def setCurrentAmount(self,currentAmountToTrade):
        self.currentAmountToTrade= currentAmountToTrade
        return self.currentAmountToTrade
    
    #def getBalance(self):
     #   return 
    
    def createPortfolio(self,stock):        
        currPrice = stock.get_price() 

    
        return "Go Pee"
        
    def checkHowMany(self,curBankAmount,currPrice): #checks how many stocks a trader can purchase
        #Use Constant for trading
        tradingFee = 10 #$10 US Dollars
        curBankAmount = float(curBankAmount)
        currPrice = float(currPrice)
        howMany = ((curBankAmount - tradingFee)/(currPrice))
        howMany = int(howMany)
        return howMany
    
    def checkWhenSell():  #need to write a function to see when should I sell 
        return null