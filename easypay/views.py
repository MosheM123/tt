import requests
import time
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm
from .models import (Products, Products_Sale, All_Products,
                     Customer, Personal_cart, Cart_item)

mc_url="https://api.thingspeak.com/update?api_key=8R3CO2HRXMICK3VK&field1="

def hi(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    template = loader.get_template('authentication/landpage.html')
    context = {
        'products': products,
        'products2':products2,
    }
    return HttpResponse(template.render(context, request))

def hi2(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    template = loader.get_template('authentication/2.html')
    context = {
        'products': products,
        'products2':products2,
    }
    return HttpResponse(template.render(context, request))

def hi2id(request, id):
    cart = Personal_cart.objects.get(id=id)
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    users = Customer.objects.all().values()
    user = Customer.objects.get(id=id)
    template = loader.get_template('authentication/2id.html')
    context = {
        'products': products,
        'products2':products2,
        'user':user,
        'users':users,
        'cart':cart,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    products =All_Products.objects.all().values()
    product = All_Products.objects.get(id=id)
    template = loader.get_template('authentication/details.html')
    context = {'product':product, 'products':products,}
    return HttpResponse(template.render(context, request))

def details2(request, id):
    customery = Customer.objects.get(id=request.user.id)
    all_items = Cart_item.objects.filter(user=customery)
    cart = Personal_cart.objects.get(id=request.user.id)
    product = All_Products.objects.get(id=id)
    products =All_Products.objects.all().values()
    template = loader.get_template('authentication/details2.html')
    count = 0
    def yap():
        if request.GET.get('Next') == 'Next':
            new_item = Cart_item(item=product, user=customery, amount=1)
            cart.quantity = cart.quantity + 1
            cart.board.append(product.id)
            cart.save()
            product.save()
    while count < 2:
        if(count == 1):
            count = count + 1
            yap()
            print(count)
    context = {'product':product, 'products':products, 'cart':cart}
    return HttpResponse(template.render(context, request))

def cart(request, id):
    products =All_Products.objects.all().values()
    cart = Personal_cart.objects.get(id=request.user.id)
    b = cart.board
    users = Customer.objects.all().values()
    doll = All_Products.objects.get(id=1)
    r = doll.id

    context={
        'products':products,
        'cart':cart,
        'users':users,
        'r':r,
        'b':b,
    }
    template = loader.get_template('authentication/cart.html')
    return HttpResponse(template.render(context,request))


def login_user(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            cart = Personal_cart.objects.get(id=user.id)
            login(request, user)
            return HttpResponseRedirect('/hi2id/%d'%user.id)

        else:
            return redirect('login_user')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('/')

def register_user(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'authentication/register_user.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            cart = Personal_cart()
            cart.save()
            login(request, user)
            context = {
                'products': products,
                'products2': products2,
                'user':user,
            }
            return HttpResponseRedirect('/hi2id/%d'%user.id)
        else:
            return render(request, 'authentication/register_user.html', {'form': form})

def age0_3(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/age0_3.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def age4_9(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/age4_9.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def age10_14(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/age10_14.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def age14plus(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/age14plus.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def log0_3(request):
    if request.user.is_authenticated:
        current_usr = request.user
        cart = Personal_cart.objects.get(id=current_usr.id)
        products = Products.objects.all().values()
        products2 = Products_Sale.objects.all().values()
        products3 = All_Products.objects.all().values()
        template = loader.get_template('authentication/log0_3.html')
        context = {
            'products': products,
            'products2': products2,
            'products3': products3,
            'cart':cart,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')

def log4_9(request):
    cart = Personal_cart.objects.get(id=request.user.id)
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/log4_9.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
        'cart':cart,
    }
    return HttpResponse(template.render(context, request))

def log10_14(request):
    cart = Personal_cart.objects.get(id=request.user.id)
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/log10_14.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
        'cart':cart,
    }
    return HttpResponse(template.render(context, request))

def log14plus(request):
    cart = Personal_cart.objects.get(id=request.user.id)
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/log14plus.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
        'cart':cart,
    }
    return HttpResponse(template.render(context, request))

def boy(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/boy.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def girl(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/girl.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def boyl(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/boyl.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))

def girll(request):
    products = Products.objects.all().values()
    products2 = Products_Sale.objects.all().values()
    products3 = All_Products.objects.all().values()
    a = 0
    template = loader.get_template('authentication/girll.html')
    context = {
        'products': products,
        'products2': products2,
        'products3': products3,
        'a' : a,
    }
    return HttpResponse(template.render(context, request))
