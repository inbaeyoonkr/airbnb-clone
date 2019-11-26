from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from . import models


class LoginForm(forms.Form):
    """ Login Form Definition"""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")


class SignUpForm(UserCreationForm):
    """ SignUp Form Definition """

    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password confirmation does not match")
        return password2

    def save(self, *args, **kwargs):
        print(self.cleaned_data)
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        user.username = email
        user.set_password(password)
        user.save()
