from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import SelfCheckIn, LuggageTracking, SpecialAssistance
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class SelfCheckInListView(View):
    def get(self, request):
        checkins = SelfCheckIn.objects.all()
        return JsonResponse({"checkins": list(checkins.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        checkin = SelfCheckIn.objects.create(
            passenger_name=data['passenger_name'],
            flight_number=data['flight_number'],
            seat_number=data['seat_number']
        )
        return JsonResponse({"checkin": checkin.id})

class LuggageTrackingListView(View):
    def get(self, request):
        luggages = LuggageTracking.objects.all()
        return JsonResponse({"luggages": list(luggages.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        luggage = LuggageTracking.objects.create(
            luggage_id=data['luggage_id'],
            passenger_name=data['passenger_name'],
            current_location=data['current_location'],
            status=data['status']
        )
        return JsonResponse({"luggage": luggage.id})

class SpecialAssistanceListView(View):
    def get(self, request):
        requests = SpecialAssistance.objects.all()
        return JsonResponse({"requests": list(requests.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        assistance = SpecialAssistance.objects.create(
            passenger_name=data['passenger_name'],
            assistance_type=data['assistance_type'],
            status=data['status']
        )
        return JsonResponse({"assistance": assistance.id})
