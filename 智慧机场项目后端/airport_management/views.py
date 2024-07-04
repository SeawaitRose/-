from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import FlightSchedule, Aircraft, CrewMember
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class FlightScheduleListView(View):
    def get(self, request):
        schedules = FlightSchedule.objects.all()
        return JsonResponse({"schedules": list(schedules.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        schedule = FlightSchedule.objects.create(
            flight_number=data['flight_number'],
            airline=data['airline'],
            departure_time=data['departure_time'],
            arrival_time=data['arrival_time'],
            status=data['status'],
            gate=data['gate']
        )
        return JsonResponse({"schedule": schedule.id})

class FlightScheduleDetailView(View):
    def get(self, request, schedule_id):
        schedule = get_object_or_404(FlightSchedule, pk=schedule_id)
        crew_members = CrewMember.objects.filter(flight=schedule)
        return JsonResponse({
            "schedule": {
                "id": schedule.id,
                "flight_number": schedule.flight_number,
                "airline": schedule.airline,
                "departure_time": schedule.departure_time,
                "arrival_time": schedule.arrival_time,
                "status": schedule.status,
                "gate": schedule.gate,
                "crew_members": list(crew_members.values())
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, schedule_id):
        schedule = get_object_or_404(FlightSchedule, pk=schedule_id)
        data = json.loads(request.body)
        schedule.flight_number = data.get('flight_number', schedule.flight_number)
        schedule.airline = data.get('airline', schedule.airline)
        schedule.departure_time = data.get('departure_time', schedule.departure_time)
        schedule.arrival_time = data.get('arrival_time', schedule.arrival_time)
        schedule.status = data.get('status', schedule.status)
        schedule.gate = data.get('gate', schedule.gate)
        schedule.save()
        return JsonResponse({"schedule": schedule.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, schedule_id):
        schedule = get_object_or_404(FlightSchedule, pk=schedule_id)
        schedule.delete()
        return JsonResponse({"deleted": True})

class AircraftListView(View):
    def get(self, request):
        aircrafts = Aircraft.objects.all()
        return JsonResponse({"aircrafts": list(aircrafts.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        aircraft = Aircraft.objects.create(
            model=data['model'],
            capacity=data['capacity'],
            airline=data['airline'],
            status=data['status']
        )
        return JsonResponse({"aircraft": aircraft.id})

class AircraftDetailView(View):
    def get(self, request, aircraft_id):
        aircraft = get_object_or_404(Aircraft, pk=aircraft_id)
        return JsonResponse({
            "aircraft": {
                "id": aircraft.id,
                "model": aircraft.model,
                "capacity": aircraft.capacity,
                "airline": aircraft.airline,
                "status": aircraft.status
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, aircraft_id):
        aircraft = get_object_or_404(Aircraft, pk=aircraft_id)
        data = json.loads(request.body)
        aircraft.model = data.get('model', aircraft.model)
        aircraft.capacity = data.get('capacity', aircraft.capacity)
        aircraft.airline = data.get('airline', aircraft.airline)
        aircraft.status = data.get('status', aircraft.status)
        aircraft.save()
        return JsonResponse({"aircraft": aircraft.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, aircraft_id):
        aircraft = get_object_or_404(Aircraft, pk=aircraft_id)
        aircraft.delete()
        return JsonResponse({"deleted": True})

class CrewMemberListView(View):
    def get(self, request):
        crew_members = CrewMember.objects.all()
        return JsonResponse({"crew_members": list(crew_members.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        flight = get_object_or_404(FlightSchedule, pk=data['flight_id'])
        crew_member = CrewMember.objects.create(
            name=data['name'],
            position=data['position'],
            flight=flight
        )
        return JsonResponse({"crew_member": crew_member.id})
