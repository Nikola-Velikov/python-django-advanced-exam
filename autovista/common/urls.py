from django.urls import path

from .views import HomePage, AboutPage, CreateMessageView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about', AboutPage.as_view(), name='about'),
    path('contact', CreateMessageView.as_view(), name='contact'),
]
