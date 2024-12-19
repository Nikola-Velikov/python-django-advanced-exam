from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .forms import CreateAutoPart, UpdateAutoPart
from .models import AutoPart


class CreateAutoPartView(LoginRequiredMixin, CreateView):
    form_class = CreateAutoPart
    success_url = reverse_lazy('auto-parts')  # Redirect to list page after creating
    template_name = 'auto_parts/create-auto-part.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Associate the auto part with the logged-in user
        return super().form_valid(form)


class AutoPartsDashboard(ListView):
    model = AutoPart
    template_name = 'auto_parts/dashboard.html'
    context_object_name = "auto_parts"


class AutoPartDetailView(DetailView):
    model = AutoPart
    template_name = 'auto_parts/details-auto-part.html'
    pk_url_kwarg = 'auto_part_id'
    context_object_name = "auto_part"


class EditAutoPartView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = UpdateAutoPart
    model = AutoPart
    success_url = reverse_lazy('auto-parts')
    template_name = 'auto_parts/edit-auto-part.html'
    pk_url_kwarg = 'auto_part_id'

    def test_func(self):
        auto_part = self.get_object()
        return self.request.user == auto_part.owner  # Ensure only the user who created the part can edit it

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            return redirect('auto_parts_list')


@login_required
def deleteAutoPart(request, auto_part_id):
    auto_part = get_object_or_404(AutoPart, id=auto_part_id)

    if request.user == auto_part.owner:
        auto_part.delete()
        return redirect('auto-parts')
    else:
        return redirect('auto-parts')
