# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:19:57 2016

@author: Cordell
"""
class Decisions:
    def determineAgainst50(self,curr,fifty):
        if(curr > fifty):
            decision = "buy"
        elif(fifty >= curr):
            decision = "sell"
        return decision
    
    def determineAgainst200(self,curr,twoHundred):
        if(curr > twoHundred):
            decision = "buy"
        elif(twoHundred >= curr):
            decision = "sell"
        return decision
        
    def getFiftyDayMoving(self,stock):
        fiftyDayMovingPrice = stock.get_50day_moving_avg()
        twoHundredMovingPrice = stock.get_200day_moving_avg()
        print(twoHundredMovingPrice)