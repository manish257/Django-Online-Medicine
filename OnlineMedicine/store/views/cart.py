from django.views import View

from tabnanny import check
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import  check_password
from store.models.patient import Patient
from django.views import View
from store.models.medicine import Medicine

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        medicines = Medicine.get_medicines_by_id(ids)
        print(medicines)
        return render(request, 'cart.html', {'medicines' : medicines} )

