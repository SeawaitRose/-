from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import PickupRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class PickupRequestListView(View):
    def get(self, request):
        requests = PickupRequest.objects.all()
        return JsonResponse({"requests": list(requests.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        pickup_request = PickupRequest.objects.create(
            passenger_name=data['passenger_name'],
            flight_number=data['flight_number'],
            pickup_location=data['pickup_location'],
            status=data['status'],
            vehicle_assigned=data.get('vehicle_assigned')
        )
        return JsonResponse({"pickup_request": pickup_request.id})

class PickupRequestDetailView(View):
    def get(self, request, request_id):
        pickup_request = get_object_or_404(PickupRequest, pk=request_id)
        return JsonResponse({
            "pickup_request": {
                "id": pickup_request.id,
                "passenger_name": pickup_request.passenger_name,
                "flight_number": pickup_request.flight_number,
                "pickup_location": pickup_request.pickup_location,
                "requested_time": pickup_request.requested_time,
                "status": pickup_request.status,
                "vehicle_assigned": pickup_request.vehicle_assigned
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, request_id):
        pickup_request = get_object_or_404(PickupRequest, pk=request_id)
        data = json.loads(request.body)
        pickup_request.passenger_name = data.get('passenger_name', pickup_request.passenger_name)
        pickup_request.flight_number = data.get('flight_number', pickup_request.flight_number)
        pickup_request.pickup_location = data.get('pickup_location', pickup_request.pickup_location)
        pickup_request.status = data.get('status', pickup_request.status)
        pickup_request.vehicle_assigned = data.get('vehicle_assigned', pickup_request.vehicle_assigned)
        pickup_request.save()
        return JsonResponse({"pickup_request": pickup_request.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, request_id):
        pickup_request = get_object_or_404(PickupRequest, pk=request_id)
        pickup_request.delete()
        return JsonResponse({"deleted": True})
