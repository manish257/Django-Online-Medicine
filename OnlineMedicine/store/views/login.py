from django.views import View

from tabnanny import check
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.patient import Patient
from django.views import View


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        patient = Patient.get_patient_by_email(email)
        error_message = None
        if patient:
            flag = check_password(password, patient.password)
            if flag:
                request.session['patient'] = patient.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Invalid Email or Password"
        else:
            error_message = "Invalid Email or Password"

        print(email, password)
        return render(request, 'login.html', {'error': error_message})
def logout(request):
    request.session.clear()
    return redirect('login')
