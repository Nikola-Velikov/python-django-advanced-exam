from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserForm
from .mixins import UnauthenticatedUserOnlyMixin


class UserRegisterView(UnauthenticatedUserOnlyMixin, CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(self.success_url)

class UserLoginView(UnauthenticatedUserOnlyMixin, LoginView):
    pass