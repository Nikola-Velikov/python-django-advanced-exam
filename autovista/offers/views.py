from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .forms import CreateOffer, UpdateOffer
from .models import Offer


class CreateOfferView(LoginRequiredMixin, CreateView):
    form_class = CreateOffer
    success_url = reverse_lazy('offers')
    template_name = 'offers/create-offer.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OffersDashboard(ListView):
    model = Offer
    template_name = 'offers/dashboard.html'
    context_object_name = "offers"


class DetailsOffer(DetailView):
    model = Offer
    template_name = 'offers/details-offer.html'
    pk_url_kwarg = 'offer_id'
    context_object_name = "offer"


class EditOffer(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = UpdateOffer
    model = Offer
    success_url = reverse_lazy('offers')
    template_name = 'offers/edit-offer.html'
    pk_url_kwarg = 'offer_id'

    def test_func(self):
        offer = self.get_object()
        return self.request.user == offer.owner

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            return redirect('offers')

@login_required
def deleteOffer(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)

    if request.user == offer.owner:
        offer.delete()
        return redirect('offers')
    else:
        return redirect('offers')
