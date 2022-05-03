from django.contrib import admin
from .models.medicine import Medicine
from .models.category import Category
from .models.patient import Patient
from .models.patient import Patient
from .models.orders import Order


class AdminMedicine(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['medicine', 'patient', 'quantity', 'price', 'date', 'status']


class AdminPatient(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']


# Register your models here.
admin.site.register(Medicine, AdminMedicine)
admin.site.register(Category, AdminCategory)
admin.site.register(Patient, AdminPatient)
admin.site.register(Order, AdminOrder)

