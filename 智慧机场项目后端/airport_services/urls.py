from django.urls import path
from .views import SelfCheckInListView, LuggageTrackingListView, SpecialAssistanceListView

urlpatterns = [
    path('checkins/', SelfCheckInListView.as_view(), name='self_checkin_list'),
    path('luggages/', LuggageTrackingListView.as_view(), name='luggage_tracking_list'),
    path('assistances/', SpecialAssistanceListView.as_view(), name='special_assistance_list'),
]
