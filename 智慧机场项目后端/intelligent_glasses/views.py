from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import GlassesUsageLog, MaintenanceTask
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class GlassesUsageLogListView(View):
    def get(self, request):
        logs = GlassesUsageLog.objects.all()
        return JsonResponse({"logs": list(logs.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        log = GlassesUsageLog.objects.create(
            user=data['user'],
            task=data['task'],
            status=data['status']
        )
        return JsonResponse({"log": log.id})

class MaintenanceTaskListView(View):
    def get(self, request):
        tasks = MaintenanceTask.objects.all()
        return JsonResponse({"tasks": list(tasks.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        task = MaintenanceTask.objects.create(
            glasses_id=data['glasses_id'],
            task_description=data['task_description'],
            assigned_to=data['assigned_to'],
            status=data['status']
        )
        return JsonResponse({"task": task.id})

class MaintenanceTaskDetailView(View):
    def get(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        return JsonResponse({
            "task": {
                "id": task.id,
                "glasses_id": task.glasses_id,
                "task_description": task.task_description,
                "assigned_to": task.assigned_to,
                "status": task.status,
                "timestamp": task.timestamp
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        data = json.loads(request.body)
        task.glasses_id = data.get('glasses_id', task.glasses_id)
        task.task_description = data.get('task_description', task.task_description)
        task.assigned_to = data.get('assigned_to', task.assigned_to)
        task.status = data.get('status', task.status)
