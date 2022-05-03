from tabnanny import check
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.medicine import Medicine
from store.models.category import Category
from store.models.patient import Patient
from django.views import View


# Create your views here.

class Index(View):

    def post(self, request):
        medicine = request.POST.get('medicine')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(medicine)

            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(medicine)
                    else:
                        cart[medicine] = quantity - 1
                else:
                    cart[medicine] = quantity + 1
            else:
                cart[medicine] = 1
        else:
            cart = {}
            cart[medicine] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        medicines = None

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            medicines = Medicine.get_all_medicines_by_categoryid(categoryID)
        else:
            medicines = Medicine.get_all_medicines()
        data = {}
        data['medicines'] = medicines
        data['categories'] = categories
        print('you are :', request.session.get('email'))
        return render(request, 'index.html', data)
