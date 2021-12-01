from django.shortcuts import render
from .models import Product , Promotion

def products(request):
    products= Product.objects.all()
    context={
        'products': products
    }
    return render(request, 'products/products.html' , context)




def promotion(request):
    promotion = Promotion.objects.all()
    context = {
        'promotion': promotion
    }
    return render(request , 'products/promotion.html' ,context)

