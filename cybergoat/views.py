from django.shortcuts import render
from cyberapp.programs import money, stocks, members
from django.contrib.auth.decorators import login_required
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
    display1 = stocks.stock_search()
    if request.method == 'POST':
        try:
            price_paid = float(request.POST['price_paid'])
            quantity = int(request.POST['quantity'])
            sell_price = float(request.POST['sell_price'])
            total_gain = stocks.stock_calc(price_paid, quantity, sell_price)
            total_gain = '{:,.2f} | Change: {:,.2f}%'.format(total_gain, stocks.percent_change(price_paid, sell_price))

            return render(request, 'stocks.html', {'total_gain':total_gain,'display1':display1})   
        
        except:
            pass

        try:
            search = request.POST['stock_search']
            display1 = stocks.stock_search(search)
            return render(request, 'stocks.html', {'display1':display1})

        except Exception:
            error = "Error! Input not understood."
            return render(request, 'stocks.html',{'error':error})

            

    return render(request, 'stocks.html',{'display1':display1})


def member(request):
    #Will be replaced with different logging mechanism
    if request.method == 'POST':
        id = request.POST['id']
        user = members.log_user(id)
    else:
        user= members.log_user()
    return render(request, 'members.html',{})


def about(request):
    return render(request, 'about.html', {})

@login_required
def login(request):
    return render(request,'test.html', {})

@login_required
def logout(request):

    return render(request,'logout.html', {})
