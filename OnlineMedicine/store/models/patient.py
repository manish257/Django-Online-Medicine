from django.db import models
from django.core.validators import MinLengthValidator


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()
    
    @staticmethod
    def get_patient_by_email(email):
        try:
            return Patient.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Patient.objects.filter(email=self.email):
            return True
    
        return False
