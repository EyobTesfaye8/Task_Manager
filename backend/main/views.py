from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import *

# Create your views here.

class TaskList(APIView):
    def get(self, request):
        tasks = load_tasks()
        return Response(tasks)

    def post(self, request):
        tasks = load_tasks()
        new_task = {
            "id": len(tasks) + 1,
            "title": request.data.get("title"),
            "completed":False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        return Response(new_task, status=status.HTTP_201_CREATED)

class TaskDetail(APIView):
    def put(self, request, id):
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == id:
                task["completed"] = True
                save_tasks(tasks)
                return Response(task)
        return Response({"error": "Task not found"}, status=404)

    def delete(self, request, id):
        tasks = load_tasks()
        tasks = [task for task in tasks if task["id"] != id]
        save_tasks(tasks)
        return Response(status=204)
