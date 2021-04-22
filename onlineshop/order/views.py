from django.shortcuts import render
from .models import *
from cart.cart import Cart
from .forms import *
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        # 입력받은 정보를 후처리
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        # 주문자 정보를 입력받는 페이지
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})