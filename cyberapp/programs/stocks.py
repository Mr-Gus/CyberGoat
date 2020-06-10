import yfinance as yf


def percent_change(original, final):
    try:
        original = float(original)
        final = float(final)
        change = final - original
        change = change / original * 100
        change = float('{:.2f}'.format(change))
        '''
        if change < 0:
            return(f'The value went from {original} to {final} and decreased by {change}')
        elif change == 0:
            return(change)
        elif change > 0:
            return(f'The value went from {original} to {final} and increased by {change}')
        '''
    except:
        change = None
    return(change)


#Program part that calculates stockprice returns. Advance version will provide best scenario.

stocks = { 'nike': [88.53, 40, 115.29], 'citi': [45.04, 42, 85.00], 'honeywell': [134.39, 31, 189.00], 'leidos': [95.45, 33, 112.00],
'starbucks':[74.89, 28, 93.00], 'abbot': [89.92,20, 98.00], 'ddog':[71.98, 22, 81.00], 'morganSan': [38.57, 41, 59.00], 'repub': [80.33, 35, 96.00],
'wastem':[108.70, 13, 114.00] }

def stock_calc(price_paid, quantity, sell_price):
    total_gain= (sell_price - price_paid) * quantity
    return total_gain

def scenario(stock=stocks, target_value=20000):
    expected_gains = 0
    personal_invested = 0
    total_investments = 0

    for name, values in stock.items():
        personal_invested += (values[0] * values[1])
        expected_gains += stock_calc(values[0],values[1], values[2])
        print()


    total_investments  = personal_invested + expected_gains

    if total_investments < target_value:
        report = 'Goals will not be met.\nPersonal investment: ${:,.2f} + Expected return: ${:,.2f} =  ${:,.2f}.\nPortfolio change: {:.2f}%'.format(personal_invested, expected_gains, (total_investments), percent_change(personal_invested,total_investments))

    elif total_investments >= target_value:
        report = 'Goals will be met.\nPersonal investment: ${:,.2f} + Expected return: ${:,.2f} = ${:,.2f}. \nPortfolio change: {:.2f}%'.format(personal_invested, expected_gains, (total_investments),percent_change(personal_invested,total_investments))
    else:
        report = None

    return(report)
