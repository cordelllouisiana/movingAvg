# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:09:06 2016

@author: Cordell
"""

from yahoo_finance import Share
#FIND OTHER libraries to USE as well 


class stockClient:
    
    def __init__(self, symb):
        self.symb= Share(symb)

    def get_price(self):
        return self.get_price()
    
#==============================================================================
#     def get_change()
#     
#     def get_volume()
#     
#     def get_prev_close()
#     
#     def get_open()
#     
#     def get_avg_daily_volume()
#     
#     def get_stock_exchange()
#     
#     def get_market_cap()
#     
#     def get_book_value()
#     
#     def get_ebitda()
#     
#     def get_dividend_share()
#     
#     def get_dividend_yield()
#     
#     def get_earnings_share()
#     
#     def get_days_high()
#     
#     def get_days_low()
#     
#     def get_year_high()
#     
#     def get_year_low()
#     
#     def get_50day_moving_avg()
#     
#     def get_200day_moving_avg()
#     
#     def get_price_earnings_ratio()
#     
#     def get_price_earnings_growth_ratio()
#     
#     def get_price_sales()
#     
#     def get_price_book()
#     
#     def get_short_ratio()
#     
#     def get_trade_datetime()
#     
#     def get_historical(start_date, end_date)
#     
#     def get_info()
#     
#     def refresh()
#==============================================================================
