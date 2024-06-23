from django.shortcuts import render
from .models import Sales
from django.shortcuts import render, redirect
from .forms import SalesForm

def home (request):
    sales = Sales.objects.all()
    return render(request, 'home.html',{'sales':sales})



def add_sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SalesForm()
    return render(request, 'add_sales.html', {'form': form})
