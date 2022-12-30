from django.shortcuts import render, redirect

# Create your views here.
from app.forms import items


def home(request):
    return render(request,'home.html')


def product_add(request):
    form = items()
    if request.method == 'POST':
        form = items(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_add')
    return render(request,'product.html',{'form':form})