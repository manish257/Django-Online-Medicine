from tabnanny import check
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from store.models.patient import Patient
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email

        }

        error_message = None

        patient = Patient(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password)

        error_message = self.validatePatient(patient)

        # save
        if not error_message:
            print(first_name, last_name)
            patient.password = make_password(patient.password)

            patient.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validatePatient(self, patient):
        error_message = None
        if (not patient.first_name):
            error_message = "Please Enter First Name"
        elif len(patient.first_name) < 4:
            error_message = "First Name should be greater than 4 characters"
        elif not patient.last_name:
            error_message = 'Please Enter Last Name'
        elif len(patient.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not patient.phone:
            error_message = 'Please Enter Phone Number'
        elif len(patient.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(patient.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(patient.email) < 5:
            error_message = 'Email must be 5 char long'
        elif patient.isExists():
            error_message = "This Email is already used"

        return error_message
