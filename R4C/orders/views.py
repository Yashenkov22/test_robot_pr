from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import OrderForm
from .models import Order
from .services import construct_data_for_order


def make_order(request: HttpRequest):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            dict_for_order, response_text = construct_data_for_order(data)
            Order.objects.create(**dict_for_order)
            
            return HttpResponse(response_text)
    
        else:
            return render(request,
                          'orders/make_order.html',
                          context={'form': form})
            
    form = OrderForm()
    
    return render(request,
                  'orders/make_order.html',
                  context={'form': form})