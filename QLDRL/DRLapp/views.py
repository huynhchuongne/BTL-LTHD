from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *


# Create your views here.

class RegulationViewSet(viewsets.ModelViewSet):
    queryset = Regulation.objects.filter(active=True)
    serializer_class = RegulationSerializer


class FalcutyViewSet(viewsets.ModelViewSet):
    queryset = Falcuty.objects.filter(active=True)
    serializer_class = FalcutySerializer


class ClassViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Class.objects.filter(active=True)
    serializer_class = ClassSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Activity.objects.filter(active=True)
    serializer_class = ActivitySerializer