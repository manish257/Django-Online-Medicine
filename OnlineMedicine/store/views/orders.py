from django.views import View

from tabnanny import check
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from store.models.patient import Patient
from django.views import View
from store.models.medicine import Medicine
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):

    def get(self, request):
        patient = request.session.get('patient')
        orders = Order.get_orders_by_patient(patient)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders' : orders})
