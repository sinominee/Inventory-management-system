from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AddProductForm
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in successfully")
            return redirect ('home')
        else:
            messages.success(request, "There was an error")
            return redirect('home')
    else:    
        return render(request, 'home.html', {'products': products})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def product_record(request, pk):
    if request.user.is_authenticated:
        product_record = Product.objects.get(id=pk)
        return render(request, 'record.html', {'product_record': product_record})
    else:
        messages.success(request, "You must be logged in to view this page.. ")
        return redirect('home')

def delete_product(request, pk):
    if request.user.is_authenticated:
        delete_it = Product.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Product deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete this ")
        return redirect('home')

def add_product(request):
    form = AddProductForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_product = form.save()
                messages.success(request, "Product Added")
                return redirect('home')
        return render(request, 'add_product.html', {'form':form})
    else:
        messages.success(request, "you must be logged In")
        return redirect('home')
    
                          
def update_product(request, pk):
    if request.user.is_authenticated:
        current_product = Product.objects.get(id=pk)
        form = AddProductForm(request.POST or None, instance=current_product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product data has been UPDATED")
            return redirect('home')
        return render(request, 'update_product.html', {'form':form})
    else:
        messages.success(request, "you must be logged")
        return redirect('home')






     
                   
                     

