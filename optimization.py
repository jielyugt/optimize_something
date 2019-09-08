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

# additional import
from scipy.optimize import minimize

# This is the function that will be tested by the autograder  		   	  			  	 		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		   	  			  	 		  		  		    	 		 		   		 		  
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		   	  			  	 		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		   	  			  	 		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		   	  			  	 		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		   	  			  	 		  		  		    	 		 		   		 		  
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later  

    prices = prices.ffill().bfill()

    # find the allocations for the optimal portfolio 
    n = len(syms)
    get_sr = lambda allocs: -get_cr_adr_sddr_sr(allocs, prices)[3]
    init_allocs = [1/n] * n
    cons = [{ "type": "eq", "fun": lambda allocs: sum(allocs) - 1}]
    bnds = [(0,1) for _ in range(n)]
    result = minimize(get_sr, init_allocs, method = "SLSQP", constraints = cons, bounds = bnds)
    optimal_allocs = result.x

    cr, adr, sddr, sr = get_cr_adr_sddr_sr(optimal_allocs, prices)
    daily_sums = get_daily_sums(optimal_allocs, prices)


    # Get daily portfolio value  		   	  			  	 		  		  		    	 		 		   		 		  
    port_val = daily_sums
    normalized_SPY = prices_SPY / prices_SPY[0]

    # Compare daily portfolio value with SPY using a normalized plot  		   	  			  	 		  		  		    	 		 		   		 		  
    if gen_plot:  		   	  			  	 		  		  		    	 		 		   		 		  
        # add code to plot here  
        df_temp = pd.concat([port_val, normalized_SPY], keys=['Portfolio', 'SPY'], axis=1)  		   	  			  	 		  		  		    	 		 		   		 		  
        ax = df_temp.plot(title = "Daily Portfolio Value and SPY", grid = True)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        plt.grid(linestyle='dotted')
        plt.savefig('output.png')

    return optimal_allocs, cr, adr, sddr, sr		  	 		  		  		    	 		 		   		 		  

# returns the cumulative return, average daily return and volatility from a portfolio
def get_cr_adr_sddr_sr(allocs, prices):

    """
    # cumulative sum is the same as starting *= (1 + each daily return)
    curr = 1
    for each in daily_returns:
        curr *= 1 + each
    print("+++++++++++++++++++++", curr - 1)
    """

    daily_sums = get_daily_sums(allocs, prices)

    # cr - cumulative return
    cr = daily_sums[-1] / daily_sums[0] - 1

    # adr - average daily return
    daily_returns = daily_sums / daily_sums.shift(1) - 1
    daily_returns = daily_returns.iloc[1:]
    adr = daily_returns.mean()

    # sddr - std of daily returns
    sddr = daily_returns.std()

    # sr - sharpe ratio
    sr = adr / sddr

    return cr, adr, sddr, sr

# returns the daily returns given stock prices and allocations
def get_daily_sums(allocs, prices):

    normalized_prices = prices.div(prices.iloc[0])
    allocs_adjusted = normalized_prices.multiply(allocs)
    daily_sum = allocs_adjusted.sum(axis = 1)

    return daily_sum	

def test_code():  		   	  			  	 		  		  		    	 		 		   		 		  
    # This function WILL NOT be called by the auto grader  		   	  			  	 		  		  		    	 		 		   		 		  
    # Do not assume that any variables defined here are available to your function/code  		   	  			  	 		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		   	  			  	 		  		  		    	 		 		   		 		  

    # Define input parameters  		   	  			  	 		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		   	  			  	 		  		  		    	 		 		   		 		  
    # the autograder!  		   	  			  	 		  		  		    	 		 		   		 		  

    """
    start_date = dt.datetime(2010,1,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2011,1,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM', 'IBM']  
    gen_plot = True
    """


    """
    # testing out hole filling feature
    # e.g. WDC has a missing value at 2002-02-01
    start_date = dt.datetime(2001,1,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2003,1,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    symbols = ['WDC', 'AAPL', 'BRCM', 'JNJ', 'IBM']  
    gen_plot = True 
    """

    # report data
    start_date = dt.datetime(2008,6,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2009,6,1)  		   	  			  	 		  		  		    	 		 		   		 		  
    symbols = ["IBM", "X", "GLD", "JPM"]  
    gen_plot = True		  	 		  		  		    	 		 		   		 		  

    # Assess the portfolio  		   	  			  	 		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = gen_plot)

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

    # run grading script locally
    # PYTHONPATH=../:. python3 grade_optimization.py

    # run grading script on buffet
    # PYTHONPATH=../:. python grade_optimization.py

