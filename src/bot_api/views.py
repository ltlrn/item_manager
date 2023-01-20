from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
