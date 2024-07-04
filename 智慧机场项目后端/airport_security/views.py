from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import SecurityCheck, SuspiciousActivity
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class SecurityCheckListView(View):
    def get(self, request):
        checks = SecurityCheck.objects.all()
        return JsonResponse({"checks": list(checks.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        check = SecurityCheck.objects.create(
            image=data['image'],
            detected_objects=data['detected_objects']
        )
        return JsonResponse({"check": check.id})

class SecurityCheckDetailView(View):
    def get(self, request, check_id):
        check = get_object_or_404(SecurityCheck, pk=check_id)
        return JsonResponse({
            "check": {
                "id": check.id,
                "image": check.image.url,
                "detected_objects": check.detected_objects,
                "timestamp": check.timestamp
            }
        })

class SuspiciousActivityListView(View):
    def get(self, request):
        activities = SuspiciousActivity.objects.all()
        return JsonResponse({"activities": list(activities.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        activity = SuspiciousActivity.objects.create(
            description=data['description'],
            image=data.get('image')
        )
        return JsonResponse({"activity": activity.id})
