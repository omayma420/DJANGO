from django.shortcuts import render
from .models  import Produit
def index (request):
    return render(request,'index.html')
def index1(request):
    produits=Produit.objects.all()
    context={'produits':produits}
    return render(request,'shop.html',context)
def index2(request):
    return render(request,'product_details.html')
def index3(request):
    return render(request,'about.html')
def index4(request):
    return render(request,'contact.html')
def index5(request):
    return render(request,'login.html')
def index6(request):
    return render(request,'cart.html')
def index7(request):
    return render(request,'confirmation.html')
def index8(request):
    return render(request,'checkout.html')