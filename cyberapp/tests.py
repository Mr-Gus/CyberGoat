'''
Testing for debt calculator

'''


import calendar
import datetime
now = datetime.datetime.now()

def percent_change(original, final):
    try:
        original = float(original)
        final = float(final)
        change = final - original
        change = change / original * 100
        change = float('{:.2f}'.format(change))
        if change < 0:
            return(f'The value went from {original} to {final} and decreased by {change}')
        elif change == 0:
            return(change)
        elif change > 0:
            return(f'The value went from {original} to {final} and increased by {change}')
    except:
        change = None
    return(change)


def card_calc(apr, balance):
    daily_apr = apr/365
    daily_aprc = daily_apr/100
    days = calendar.monthrange(now.year, now.month)[1]
    monthly_interest = balance * days * daily_aprc #per month
    monthly_interest = float('{:.2f}'.format(monthly_interest))

    return(monthly_interest)



def payoff_time(balance, months, apr):
    monthly_payment = []
    mths_left = months
    total_interest = []
    for x in range(0,months):
            print(f'\n\nMonths left: {mths_left}')
            interest = float(card_calc(apr,balance))
            print('Balance: {:.2f}'.format(balance))

            balance += interest
            print('Balance w interest: {:.2f}'.format(balance))
            minimum = balance/mths_left
            if minimum < 0:
                minimum = balance
            print('Minimum: {:.2f}'.format(minimum))
            monthly_payment.append(minimum)
            balance -= minimum
            print('Balance left: {:.2f}'.format(balance))
            total_interest.append(interest)
            mths_left -= 1


    minimum = float('{:.2f}'.format(minimum))
    print('\nTotal interest: {:.2f}'.format(sum(total_interest)))
    print('Monthly payment: ${:.2f}'.format(sum(monthly_payment)/len(monthly_payment)))

    return minimum
