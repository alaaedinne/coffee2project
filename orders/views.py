from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Order ,OrderDetails
from products.models import Product , Promotion
from datetime import datetime

def add_to_cart(request):
    if request.method =='GET' and 'btnadd' in request.GET and request.user.is_authenticated :
        pro_id = request.GET['pro_id']
        order = Order.objects.all().filter(user = request.user , is_finished = False)
        if Product.objects.all().filter(id = pro_id).exists() :
            pro = Product.objects.get(id=pro_id)
            #####################################
            if order:
                old_order = Order.objects.get(user =request.user ,is_finished =False)
                if OrderDetails.objects.all().filter(product=pro).exists(): 
                    messages.error(request , 'this product is added before')
                else:
                    orderdetails= OrderDetails.objects.create(product =pro, order = old_order, price=pro.price)
                    messages.success(request , 'was added to cart for old order')
            else:
                new_order = Order()
                new_order.user = request.user
                new_order.order_date = datetime.now()
                new_order.is_finished = False
                new_order.save()
                orderdetails = OrderDetails.objects.create(product= pro , order= new_order , price = pro.price)
                messages.success(request , 'was added to cart for new order')
            return redirect('products')
        elif Promotion.objects.all().filter(id= pro_id).exists():
            pro = Promotion.objects.get(id=pro_id)
        
            if order:
                old_order = Order.objects.get(user =request.user ,is_finished =False)
                if OrderDetails.objects.all().filter(promotion=pro).exists(): 
                    messages.error(request , 'this product is added before')
                else:
                    orderdetails= OrderDetails.objects.create(promotion =pro, order = old_order, price=pro.price)
                    messages.success(request , 'was added to cart for old order')
            else:
                new_order = Order()
                new_order.user = request.user
                new_order.order_date = datetime.now()
                new_order.is_finished = False
                new_order.save()
                orderdetails = OrderDetails.objects.create(promotion= pro , order= new_order , price = pro.price)
                messages.success(request , 'was added to cart for new order')
            return redirect('products')    
        else:
            return redirect('products')
    else:
        return redirect('products')
    

def cart(request):
    context=None
    if request.user.is_authenticated and not request.user.is_anonymous :
        if Order.objects.all().filter(user = request.user, is_finished= False):
            order = Order.objects.get(user = request.user, is_finished= False)
            orderdetails= OrderDetails.objects.all().filter(order= order)
            context= {
                'order': order,
                'orderdetails': orderdetails,
            }
    return render(request , 'orders/cart.html', context)

def delete_from_cart(request ,orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id :
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            orderdetails.delete()
    return redirect('cart')