from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import MaintenanceTask, MaintenanceLog
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class TaskListView(View):
    def get(self, request):
        tasks = MaintenanceTask.objects.all()
        return JsonResponse({"tasks": list(tasks.values())})

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        task = MaintenanceTask.objects.create(
            task_name=data['task_name'],
            description=data['description'],
            status=data['status'],
            assigned_to=data['assigned_to']
        )
        return JsonResponse({"task": task.id})

class TaskDetailView(View):
    def get(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        logs = MaintenanceLog.objects.filter(task=task)
        return JsonResponse({
            "task": {
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "assigned_to": task.assigned_to,
                "created_at": task.created_at,
                "updated_at": task.updated_at,
                "logs": list(logs.values())
            }
        })

    @method_decorator(csrf_exempt)
    def put(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        data = json.loads(request.body)
        task.task_name = data.get('task_name', task.task_name)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        task.assigned_to = data.get('assigned_to', task.assigned_to)
        task.save()
        return JsonResponse({"task": task.id})

    @method_decorator(csrf_exempt)
    def delete(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        task.delete()
        return JsonResponse({"deleted": True})

class LogListView(View):
    def get(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        logs = MaintenanceLog.objects.filter(task=task)
        return JsonResponse({"logs": list(logs.values())})

    @method_decorator(csrf_exempt)
    def post(self, request, task_id):
        task = get_object_or_404(MaintenanceTask, pk=task_id)
        data = json.loads(request.body)
        log = MaintenanceLog.objects.create(
            task=task,
            details=data['details']
        )
        return JsonResponse({"log": log.id})
