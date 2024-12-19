from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import MessageForm
from .models import Message


class HomePage(TemplateView):
    template_name = 'common/home.html'


class AboutPage(TemplateView):
    template_name = 'common/about.html'


class CreateMessageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'common/contact-us.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial.update({
                'name': self.request.user.username,
                'email': self.request.user.email,
            })
        return initial

    def form_valid(self, form):
        messages.success(self.request, "Your message has been successfully sent!")
        return super().form_valid(form)