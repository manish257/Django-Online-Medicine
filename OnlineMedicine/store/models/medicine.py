from django.db import models
from .category import Category


class Medicine(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/medicines/')

    @staticmethod
    def get_medicines_by_id(ids):
        return Medicine.objects.filter(id__in=ids)

    @staticmethod
    def get_all_medicines():
        return Medicine.objects.all()

    @staticmethod
    def get_all_medicines_by_categoryid(category_id):
        if category_id:
            return Medicine.objects.filter(category=category_id)
        else:
            return Medicine.get_all_medicines()
