from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    deleteBlog,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
     path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog-edit'),
     path('<int:pk>/delete/', deleteBlog, name='blog-delete'),
]
