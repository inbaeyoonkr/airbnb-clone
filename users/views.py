from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    """ Login View Definition """

    def get(self, request):
        form = forms.LoginForm(initial={"email": "iby2455@gmail.com"})
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        return render(request, "users/login.html", context={"form": form})
