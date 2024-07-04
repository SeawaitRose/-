from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Flight, GateAssignment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class FlightListView(View):
    def get(self, request):
        flights = Flight.objects.all()
        return JsonResponse({"flights": list(flights.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        flight = Flight.objects.create(
            flight_number=data['flight_number'],
            airline=data['airline'],
            departure_airport=data['departure_airport'],
            arrival_airport=data['arrival_airport'],
            departure_time=data['departure_time'],
            arrival_time=data['arrival_time'],
            status=data['status']
        )
        return JsonResponse({"flight": flight.id})

class FlightDetailView(View):
    def get(self, request, flight_id):
        flight = get_object_or_404(Flight, pk=flight_id)
        return JsonResponse({
            "flight": {
                "id": flight.id,
                "flight_number": flight.flight_number,
                "airline": flight.airline,
                "departure_airport": flight.departure_airport,
                "arrival_airport": flight.arrival_airport,
                "departure_time": flight.departure_time,
                "arrival_time": flight.arrival_time,
                "status": flight.status
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, flight_id):
        flight = get_object_or_404(Flight, pk=flight_id)
        data = json.loads(request.body)
        flight.flight_number = data.get('flight_number', flight.flight_number)
        flight.airline = data.get('airline', flight.airline)
        flight.departure_airport = data.get('departure_airport', flight.departure_airport)
        flight.arrival_airport = data.get('arrival_airport', flight.arrival_airport)
        flight.departure_time = data.get('departure_time', flight.departure_time)
        flight.arrival_time = data.get('arrival_time', flight.arrival_time)
        flight.status = data.get('status', flight.status)
        flight.save()
        return JsonResponse({"flight": flight.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, flight_id):
        flight = get_object_or_404(Flight, pk=flight_id)
        flight.delete()
        return JsonResponse({"deleted": True})

class GateAssignmentListView(View):
    def get(self, request):
        assignments = GateAssignment.objects.all()
        return JsonResponse({"assignments": list(assignments.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        flight = get_object_or_404(Flight, pk=data['flight_id'])
        assignment = GateAssignment.objects.create(
            flight=flight,
            gate=data['gate']
        )
        return JsonResponse({"assignment": assignment.id})

class GateAssignmentDetailView(View):
    def get(self, request, assignment_id):
        assignment = get_object_or_404(GateAssignment, pk=assignment_id)
        return JsonResponse({
            "assignment": {
                "id": assignment.id,
                "flight": assignment.flight.flight_number,
                "gate": assignment.gate,
                "assignment_time": assignment.assignment_time
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, assignment_id):
        assignment = get_object_or_404(GateAssignment, pk=assignment_id)
        data = json.loads(request.body)
        flight = get_object_or_404(Flight, pk=data.get('flight_id', assignment.flight.id))
        assignment.flight = flight
        assignment.gate = data.get('gate', assignment.gate)
        assignment.save()
        return JsonResponse({"assignment": assignment.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, assignment_id):
        assignment = get_object_or_404(GateAssignment, pk=assignment_id)
        assignment.delete()
        return JsonResponse({"deleted": True})
