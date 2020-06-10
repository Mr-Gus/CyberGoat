from django.shortcuts import render
from cyberapp.programs import money, stocks
import subprocess
import os


def home(request):
    try:
        #if os.path.getsize('static/images/graph.png') > 0:
        subprocess.call('rm static/images/graph.png',shell=True)
    except Exception:
        pass
    if request.method == 'POST':
        try:
            balance = float(request.POST['balance'])
            apr = float(request.POST['apr'])
            minimum = float(request.POST['minimum'])
            graph, report = money.interest_calc(apr, balance, minimum)    
            
            return render(request, 'index.html',{'graph':graph, 'report':report})
        
        except Exception:
            error = "Error! Input not understood."
            return render(request, 'index.html',{'error':error})


    return render(request, 'index.html',{})

def stockPage(request):
    if request.method == 'POST':
        try:
            price_paid = float(request.POST['price_paid'])
            quantity = int(request.POST['quantity'])
            sell_price = float(request.POST['sell_price'])
            total_gain = stocks.stock_calc(price_paid, quantity, sell_price)
            total_gain = '{:,.2f} | Change: {:,.2f}%'.format(total_gain, stocks.percent_change(price_paid, sell_price))
            
            return render(request, 'stocks.html', {'total_gain':total_gain})
     
        except Exception:
            error = 'Error! Input not understoood'
            return render(request, 'stocks.html', {'error':error})


    return render(request, 'stocks.html',{})


def about(request):
    return render(request, 'about.html', {})


def login(request):
    return render(request,'test.html', {})

def logout(request):

    return render(request,'logout.html', {})
