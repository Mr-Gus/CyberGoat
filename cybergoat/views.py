from django.shortcuts import render
from cyberapp.programs import money, stocks, members, sitemap
from django.contrib.auth.decorators import login_required
import datetime
import subprocess
import os


def home(request):
    description, keyword, name = sitemap.site_description()
    print(description)
    return render(request, 'index.html',{'description':description, 'keyword': keyword, 'name':name})


def stockPage(request):
    display1 = stocks.stock_search()
    if request.method == 'POST':
        try:
            price_paid = float(request.POST['price_paid'])
            quantity = int(request.POST['quantity'])
            sell_price = float(request.POST['sell_price'])
            total_gain, amount_invested = stocks.stock_calc(price_paid, quantity, sell_price)
            total_gain = '{:,.2f} | Change: {:,.2f}%'.format(total_gain, stocks.percent_change(price_paid, sell_price))
            amount_invested = '{:,.2f}'.format(amount_invested)
            return render(request, 'stocks.html', {'total_gain':total_gain,'amount_invested':amount_invested, 'display1':display1})   
        
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


def finance(request):
    month = datetime.datetime.now()
    month = month.strftime("%B")    

    try:
        subprocess.call('rm static/images/graph.png',shell=True)
    except Exception:
        pass
    if request.method == 'POST':
        try:
            balance = float(request.POST['balance'])
            apr = float(request.POST['apr'])
            minimum = float(request.POST['minimum'])
            graph, report = money.interest_calc(apr, balance, minimum)
            
            return render(request, 'finance.html',{'graph':graph, 'report':report})
        
        except Exception:
            error = "Error! Input not understood."
            return render(request, 'finance.html',{'error':error})

    return render(request, 'finance.html',{'month':month})



def about(request):
    return render(request, 'about.html', {})



def login(request):
    return render(request,'member.html', {})

@login_required
def member(request):
    return render(request,'member.html', {})



@login_required
def logout(request):

    return render(request,'logout.html', {})
