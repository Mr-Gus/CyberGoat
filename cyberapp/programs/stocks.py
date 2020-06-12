import yfinance as yf
import random


def percent_change(original, final):
    try:
        original = float(original)
        final = float(final)
        change = final - original
        change = change / original * 100
        change = float('{:.2f}'.format(change))
     
    except:
        change = None
    return(change)



def stock_calc(price_paid, quantity, sell_price):
    total_gain= (sell_price - price_paid) * quantity

    return total_gain


stocks = ['HON','RSG','MSFT','AAPL','C','JPM','V','NKE','LMT','LDOS','TMUS','ABT','PYPL','SBUX','MS']
stock_pick = random.choice(stocks)

def stock_search(search=stock_pick):

    display1 = yf.Ticker(search)
    display1 = display1.info
  
    return display1

