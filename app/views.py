from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def home(request):
 topwear = Product.objects.filter(category ='TW')
 bottomwear = Product.objects.filter(category ='BW')
 mobile = Product.objects.filter(category ='M')
 laptop = Product.objects.filter(category ='L')
 return render(request, 'app/home.html', {
  'mobile': mobile,
  'topwear':topwear,
  'laptop': laptop,
  'bottomwear': bottomwear
 })

def product_detail(request, id):
 product = Product.objects.get(id = id)
 return render(request, 'app/productdetail.html',{
  'product':product
 })

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
 if data == None:
   mobiles = Product.objects.filter(category = 'M')
 elif data == 'Apple' or data == 'Samsung':
    mobiles = Product.objects.filter(category = 'M').filter(brand = data)
 elif data == 'below':
    mobiles = Product.objects.filter(category = 'M').filter(discounted_price__lt = 20000)
 elif data == 'Above':
    mobiles = Product.objects.filter(category = 'M').filter(discounted_price__gt = 20000)
 return render(request, 'app/mobile.html', {
  'mobiles' : mobiles
 })

def login_view(request):
 if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('login')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        login(request, user)
        return redirect('home')
 return render(request, 'app/login.html')

def customerregistration(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('register')
        if not cpassword:
            messages.error(request, 'Confirm Password is required')
            return redirect('register')
        if not email:
            messages.error(request, 'Email is required')
            return redirect('register')
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('register')
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
 
    return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
