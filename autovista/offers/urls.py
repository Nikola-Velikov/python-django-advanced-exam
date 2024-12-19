from django.urls import path, include

from .views import CreateOfferView, OffersDashboard, DetailsOffer, EditOffer, deleteOffer

urlpatterns = [
    path('create-offer/', CreateOfferView.as_view(), name='create-offer'),
    path('catalog/', OffersDashboard.as_view(), name='offers'),
    path('<int:offer_id>/', include([
        path('details/', DetailsOffer.as_view(), name='details-offer'),
        path('edit/', EditOffer.as_view(), name='edit-offer'),
        path('delete/', deleteOffer, name='delete-offer'),

    ]))
]