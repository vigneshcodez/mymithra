from django.shortcuts import render,redirect
from .models import Category, SubCategory, Product,Awards
from . form import MessagesForm
from django.contrib import messages

# Create your views here.


def home(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.filter(sub_category_of__id=1)
    form = MessagesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Message sent...")
            return redirect('home')
    return render(request, 'pages/home.html', {'category': category, 'subcategory': subcategory,'form':form})


def about(request):
    return render(request, 'pages/about.html', {})


def subcategory(request, pk):
    category = pk
    subcategory = SubCategory.objects.filter(sub_category_of__name=pk)
    return render(request, 'pages/subcategory.html', {'subcategory': subcategory, 'category': category})


def products(request, pk):
    subcategory = pk
    products = Product.objects.filter(product_of__name=pk)
    return render(request, 'pages/product.html', {'products': products, 'subcategory': subcategory})


def detailedview(request, pk):
    product = Product.objects.get(name=pk)
    return render(request, 'pages/productdetailedview.html', {'product': product})

def awards(request):
    awards = Awards.objects.all()
    return render(request,'pages/awards.html',{"awards":awards})