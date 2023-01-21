from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer

    @action(detail=False, url_path="give-image")
    def give_image(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
