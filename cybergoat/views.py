from django.shortcuts import render
from cyberapp.programs import money
import subprocess
import os

def login(request):
    return render(request,'test.html', {})

def logout(request):

    return render(request,'logout.html', {})

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

def about(request):
    return render(request, 'about.html', {})
       