from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, reverse


class EmailLogInOnlyView(UserPassesTestMixin):
    """ Email Log In Only View Definition """

    def test_func(self):
        return self.request.user.login_method == "Email"

    def handle_no_permission(self):
        messages.error(self.request, _("Can't go there"))
        return redirect("core:home")


class LoggedOutOnlyView(UserPassesTestMixin):
    """ Logged Out Only View Mixin Definition """

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect(reverse("core:home"))


class LoggedInOnlyView(LoginRequiredMixin):
    """ Logged In Only View Definition """

    """ 
        redirect to login page person who doesn't logged in.
    """

    login_url = reverse_lazy("users:login")
