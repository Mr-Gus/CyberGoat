from matplotlib import pyplot as plt
import numpy as np

def interest_calc(apr, balance, minimum):

    plt.clf() #clears graph
    time=[]
    amount=[]
    original_balance = balance
   
    if apr > 1:
        apr /= 100

    monthly_interest_rate = apr/12
    interest=[] #array holds interest
    total_interest = 0      #sum of all interest
    loop = True
    payments = 1
    while balance > minimum and loop:
        monthly_interest = monthly_interest_rate * balance

        if balance > original_balance :
            report = 'Debt can\'t be repaid/obligation greater than 30 years. Try increasing the minimum payment.'
            graph = None
            loop = False


        else:
            balance += monthly_interest 
            balance -= minimum
            payments +=1
            
            time.append(payments)
            amount.append(balance)
            interest.append(monthly_interest)
            
            #convert arrays to numpy
            np_time = np.array(time)  
            np_amount = np.array(amount) 
            np_interest = np.array(interest) 

    #plot info
    payoff = payments/12
    plt.plot(np_time, np_amount, color='red')
    plt.plot(np_time, np_interest, color='black')
    ax= plt.subplot(111)
    ax.plot(np_time,np_amount, label='Debt', color='red')
    ax.plot(np_time,np_interest, label='Interest', color='black')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)
    plt.xlabel('Months')
    plt.ylabel('Balance ($)')
    plt.title('Amortization Graph')
    plt.grid(True)
    graph = plt.savefig('static/images/graph.png')
    if loop is True:
        report= 'It will take {:.2f} year(s) to pay this debt off.\n Estimated total interest: ${:,.2f}.'.format(payoff, sum(np_interest))
    return(graph,report)




