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
    amount_invested = price_paid * quantity

    return total_gain, amount_invested


stocks = ['MSFT','AAPL','JPM','V','NKE','LMT','LDOS','ABT','PYPL','SBUX','T',
 'MA','AAL','DIS','ABBV','NOW','DXCM', 'ADDYY','WMT']

def stock_search(search=random.choice(stocks)):
    
    display1 = yf.Ticker(search)
    display1 = display1.info
    try:
        if display1['dividendYield']:
            display1['dividendYield'] *= 100
            display1['dividendYield'] = float('{:.2f}'.format(display1['dividendYield']))
        if display1['bookValue']:
            display1['bookValue'] = float('{:.2f}'.format(display1['bookValue']))
        display1['ask']= '{:,.2f}'.format(display1['ask'])
        display1['bid'] = '{:,.2f}'.format(display1['bid'])

        display1['dayHigh'] = '{:,.2f}'.format(display1['dayHigh'])
        display1['dayLow'] = '{:,.2f}'.format(display1['dayLow'])

        display1['fiftyTwoWeekHigh'] = '{:,.2f}'.format(display1['fiftyTwoWeekHigh'])
        display1['fiftyTwoWeekLow'] = '{:,.2f}'.format(display1['fiftyTwoWeekLow'])

    except Exception:
        pass 

    return display1


stock_search()