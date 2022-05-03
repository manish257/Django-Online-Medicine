from django.views import View

from tabnanny import check
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from store.models.patient import Patient
from django.views import View
from store.models.medicine import Medicine
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        patient = request.session.get('patient')
        cart = request.session.get('cart')
        medicines = Medicine.get_medicines_by_id(list(cart.keys()))
        print(address, phone, patient, cart, medicines)

        for medicine in medicines:
            order = Order(patient=Patient(id=patient),
                          medicine=medicine,
                          price=medicine.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(medicine.id)))
            order.placeOrder();
        request.session['cart'] = {}
        return redirect('cart')
