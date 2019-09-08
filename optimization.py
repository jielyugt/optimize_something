"""MC1-P2: Optimize a portfolio.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			  	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			  	 		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			  	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			  	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			  	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			  	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			  	 		  		  		    	 		 		   		 		  
or edited.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		   	  			  	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			  	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			  	 		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Student Name: Jie Lyu 		   	  			  	 		  		  		    	 		 		   		 		  
GT User ID: jlyu31  		   	  			  	 		  		  		    	 		 		   		 		  
GT ID: 903329676  		   	  			  	 		  		  		    	 		 		   		 		  
"""  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
import pandas as pd  		   	  			  	 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		   	  			  	 		  		  		    	 		 		   		 		  
import numpy as np  		   	  			  	 		  		  		    	 		 		   		 		  
import datetime as dt  		   	  			  	 		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		   	  			  	 		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		   	  			  	 		  		  		    	 		 		   		 		  
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		   	  			  	 		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		   	  			  	 		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		   	  			  	 		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		   	  			  	 		  		  		    	 		 		   		 		  
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later  

    print("\n=========optimize_portfolio()=====================\n")		   	  			  	 		  		  		    	 		 		   		 		  
    print(prices_all.head(10))
    print("\n==================================================\n")	

    

    # find the allocations for the optimal portfolio 

    # note that the values here ARE NOT meant to be correct for a test case  
    # for debugging purpose		   	  			  	 		  		  		    	 		 		   		 		  
    allocs = np.asarray([0.3, 0.1, 0.1, 0.3, 0.2]) # add code here to find the allocations  		   	  			  	 		  		  		    	 		 		   		 		  
    cr, adr, sddr, sr = [0.25, 0.001, 0.0005, 2.1] # add code here to compute stats  		   	  			  	 		  		  		    	 		 		   		 		  
    daily_returns = get_daily_sums(allocs, prices)


    # Get daily portfolio value  		   	  			  	 		  		  		    	 		 		   		 		  
    port_val = prices_SPY # add code here to compute daily portfolio values  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		   	  			  	 		  		  		    	 		 		   		 		  
    if gen_plot:  		   	  			  	 		  		  		    	 		 		   		 		  
        # add code to plot here  		   	  			  	 		  		  		    	 		 		   		 		  
        df_temp = pd.concat([port_val, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)  		   	  			  	 		  		  		    	 		 		   		 		  
        pass  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    return allocs, cr, adr, sddr, sr  		   	  			  	 		  		  		    	 		 		   		 		  

# short and sweet function that returns the SR from a portfolio
# for use of tranning specifically
def get_sr(daily_returns):
    print("do something")

# returns the cumulative return, average daily return and volatility from a portfolio
def get_cr_adr_sddr(daily_returns):


    print("do more")

# returns the daily returns given stock prices and allocations
def get_daily_sums(allocs, prices):

    normalized_prices = prices.div(prices.iloc[0])
    allocs_adjusted = normalized_prices.multiply(allocs)
    daily_sum = allocs_adjusted.sum(axis = 1)

    """
    print("\n=============get_daily_returns====================\n")	
    print(allocs)	
    print(normalized_prices.head(10))
    print(allocs_adjusted.head(10))
    print(daily_sum.head(10))
    print(daily_sum[-1])
    print("\n==================================================\n")
    """

    return daily_sum	



def test_code():  		   	  			  	 		  		  		    	 		 		   		 		  
    # This function WILL NOT be called by the auto grader  		   	  			  	 		  		  		    	 		 		   		 		  
    # Do not assume that any variables defined here are available to your function/code  		   	  			  	 		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    # Define input parameters  		   	  			  	 		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		   	  			  	 		  		  		    	 		 		   		 		  
    # the autograder!  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2009,1,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2010,1,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM', 'IBM']  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    # Assess the portfolio  		   	  			  	 		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = False)  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    # Print statistics  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"End Date: {end_date}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Symbols: {symbols}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Allocations:{allocations}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Sharpe Ratio: {sr}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Volatility (stdev of daily returns): {sddr}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Average Daily Return: {adr}")  		   	  			  	 		  		  		    	 		 		   		 		  
    print(f"Cumulative Return: {cr}")  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			  	 		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		   	  			  	 		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		   	  			  	 		  		  		    	 		 		   		 		  
    test_code()  		   	  			  

    # test out locally
    # PYTHONPATH=../:. python3 optimization.py	

    # run grading script on buffet
    # PYTHONPATH=../:. python grade_analysis.py
		  		    	 		 		   		 		  
