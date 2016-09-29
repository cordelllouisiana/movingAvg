# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:19:57 2016

@author: Cordell
"""

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