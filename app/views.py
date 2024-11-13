from django.shortcuts import render
from .models import * 


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

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
