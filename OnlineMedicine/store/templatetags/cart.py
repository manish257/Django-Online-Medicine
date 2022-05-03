from django import template

register = template.Library()

@register.filter(name= 'is_in_cart')

def is_in_cart(medicine, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == medicine.id:
            return True
    return False;


@register.filter(name= 'cart_quantity')

def cart_quantity(medicine, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == medicine.id:
            return cart.get(id)
    return 0;

@register.filter(name= 'price_total')
def price_total(medicine, cart):
    return medicine.price * cart_quantity(medicine, cart)

@register.filter(name= 'total_cart_price')
def total_cart_price(medicines, cart):
    sum = 0;
    for m in medicines:
        sum += price_total(m, cart)
    return sum   
