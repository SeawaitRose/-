from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import FireEmergency, TerroristAttack, NaturalDisaster
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class FireEmergencyListView(View):
    def get(self, request):
        emergencies = FireEmergency.objects.all()
        return JsonResponse({"fire_emergencies": list(emergencies.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        emergency = FireEmergency.objects.create(
            location=data['location'],
            status=data['status'],
            response_team=data['response_team']
        )
        return JsonResponse({"fire_emergency": emergency.id})

class FireEmergencyDetailView(View):
    def get(self, request, emergency_id):
        emergency = get_object_or_404(FireEmergency, pk=emergency_id)
        return JsonResponse({
            "fire_emergency": {
                "id": emergency.id,
                "location": emergency.location,
                "reported_time": emergency.reported_time,
                "status": emergency.status,
                "response_team": emergency.response_team
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, emergency_id):
        emergency = get_object_or_404(FireEmergency, pk=emergency_id)
        data = json.loads(request.body)
        emergency.location = data.get('location', emergency.location)
        emergency.status = data.get('status', emergency.status)
        emergency.response_team = data.get('response_team', emergency.response_team)
        emergency.save()
        return JsonResponse({"fire_emergency": emergency.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, emergency_id):
        emergency = get_object_or_404(FireEmergency, pk=emergency_id)
        emergency.delete()
        return JsonResponse({"deleted": True})

class TerroristAttackListView(View):
    def get(self, request):
        attacks = TerroristAttack.objects.all()
        return JsonResponse({"terrorist_attacks": list(attacks.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        attack = TerroristAttack.objects.create(
            location=data['location'],
            status=data['status'],
            response_team=data['response_team']
        )
        return JsonResponse({"terrorist_attack": attack.id})

class TerroristAttackDetailView(View):
    def get(self, request, attack_id):
        attack = get_object_or_404(TerroristAttack, pk=attack_id)
        return JsonResponse({
            "terrorist_attack": {
                "id": attack.id,
                "location": attack.location,
                "reported_time": attack.reported_time,
                "status": attack.status,
                "response_team": attack.response_team
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, attack_id):
        attack = get_object_or_404(TerroristAttack, pk=attack_id)
        data = json.loads(request.body)
        attack.location = data.get('location', attack.location)
        attack.status = data.get('status', attack.status)
        attack.response_team = data.get('response_team', attack.response_team)
        attack.save()
        return JsonResponse({"terrorist_attack": attack.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, attack_id):
        attack = get_object_or_404(TerroristAttack, pk=attack_id)
        attack.delete()
        return JsonResponse({"deleted": True})

class NaturalDisasterListView(View):
    def get(self, request):
        disasters = NaturalDisaster.objects.all()
        return JsonResponse({"natural_disasters": list(disasters.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        disaster = NaturalDisaster.objects.create(
            disaster_type=data['disaster_type'],
            location=data['location'],
            status=data['status'],
            response_team=data['response_team']
        )
        return JsonResponse({"natural_disaster": disaster.id})

class NaturalDisasterDetailView(View):
    def get(self, request, disaster_id):
        disaster = get_object_or_404(NaturalDisaster, pk=disaster_id)
        return JsonResponse({
            "natural_disaster": {
                "id": disaster.id,
                "disaster_type": disaster.disaster_type,
                "location": disaster.location,
                "reported_time": disaster.reported_time,
                "status": disaster.status,
                "response_team": disaster.response_team
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, disaster_id):
        disaster = get_object_or_404(NaturalDisaster, pk=disaster_id)
        data = json.loads(request.body)
        disaster.disaster_type = data.get('disaster_type', disaster.disaster_type)
        disaster.location = data.get('location', disaster.location)
        disaster.status = data.get('status', disaster.status)
        disaster.response_team = data.get('response_team', disaster.response_team)
        disaster.save()
        return JsonResponse({"natural_disaster": disaster.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, disaster_id):
        disaster = get_object_or_404(NaturalDisaster, pk=disaster_id)
        disaster.delete()
        return JsonResponse({"deleted": True})
