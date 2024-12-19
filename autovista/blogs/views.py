from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import EditBlogForm, CreateBlogForm
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = CreateBlogForm
    template_name = 'blog/create-blog.html'
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)




class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'blog/edit-blog.html'
    success_url = reverse_lazy('blog-list')

    def test_func(self):
        offer = self.get_object()
        return self.request.user == offer.owner

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            return redirect('blog-list')


@login_required
def deleteBlog(request, pk):
    offer = get_object_or_404(Blog, id=pk)

    if request.user == offer.owner:
        offer.delete()
        return redirect('blog-list')
    else:
        return redirect('blog-list')
