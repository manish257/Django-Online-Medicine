from django.contrib import admin
from django.urls import path
from .views import login, signup
from .views.login import logout
from .views.home import Index
# from .views.signup import Signup
# from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
# from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.orders import OrderView


urlpatterns = [
    #path('', home.index, name='homepage'),
    # path('signup', signup),
    path('login', login.Login.as_view(), name='login'),
    path('', Index.as_view(), name='homepage'),
    # path('store', store , name='store'),
    #
    path('signup', signup.Signup.as_view(), name='signup'),
    # path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    # path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders')
    # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
