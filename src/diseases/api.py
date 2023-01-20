from rest_framework import status # отдается в ответах
from rest_framework.authentication import (BasicAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from diseases.models import Disease

from .serializers import DiseaseSerializer

class DiseaseView(ModelViewSet):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    # def post(self, request, *args, **kwargs):
    #     if request.user.is_anonymous:
    #         request.user = None
    #     Echo.objects.create(data=request.data, user=request.user)
    #     return Response(request.data, status=status.HTTP_201_CREATED)
