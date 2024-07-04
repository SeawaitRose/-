from django.urls import path
from .views import PickupRequestListView, PickupRequestDetailView

urlpatterns = [
    path('requests/', PickupRequestListView.as_view(), name='pickup_request_list'),
    path('requests/<int:request_id>/', PickupRequestDetailView.as_view(), name='pickup_request_detail'),
]
