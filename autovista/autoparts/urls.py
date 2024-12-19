from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAutoPartView.as_view(), name='create-auto-part'),
    path('dashboard/', views.AutoPartsDashboard.as_view(), name='auto-parts'),
    path('<int:auto_part_id>/', views.AutoPartDetailView.as_view(), name='auto-part-detail'),
    path('<int:auto_part_id>/edit/', views.EditAutoPartView.as_view(), name='edit-auto-part'),
    path('<int:auto_part_id>/delete/', views.deleteAutoPart, name='delete-auto-part'),
]
